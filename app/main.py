import json
import os
import uuid

import pdfplumber
import uvicorn
from fastapi import FastAPI, File, HTTPException, UploadFile
from models import Box, Page, Template, Word
from sanity import sanity


def extract_page(pdf_path: str) -> list[Page]:
    pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            pages.append(
                Page(
                    width=page.width,
                    height=page.height,
                    words=[Word(**word) for word in page.extract_words()],
                )
            )
    return pages


def extract_text(words: list[Word], box: Box) -> str:
    result = []
    for word in words:
        if (box.x <= word.x0 and word.x0 <= box.x + box.width) and (
            box.y <= word.top and word.top <= box.y + box.height
        ):
            result.append(word.text)
    return " ".join(result)


def process_pdf(template: Template, pdf_path: str):
    pages = extract_page(pdf_path)
    if not pages:
        raise ValueError("Erro ao extrair texto das páginas")

    model = {"template_name": template.name}

    for box in template.fields:
        value = extract_text(pages[box.page].words, box)
        for snt in box.sanities:
            value = sanity(snt, value)

        model.update({box.name: value})

    return model


app = FastAPI()
UPLOAD_DIR = "./uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/")
async def process_file(template: Template | str, file: UploadFile = File(...)):
    template_dict = json.loads(template)
    template = Template(**template_dict)

    if file.content_type != "application/pdf":
        raise HTTPException(400, "Aceito somente arquivos PDF")

    filename = f"{uuid.uuid4()}.pdf"
    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as f:
        while chunk := await file.read(1024 * 1024):
            f.write(chunk)

    try:
        result = process_pdf(template, file_path)
        return result
    except Exception as e:
        raise HTTPException(403, f"Erro ao processar PDF: {e}")

    finally:
        os.remove(file_path)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
