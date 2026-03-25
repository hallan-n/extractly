import pdfplumber
from models import Box, Page, Template, Word
from sanity import sanity


def extract_page(pdf_path) -> list[Page]:
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
        if (
            box.x <= word.x0 <= box.x + box.width
            and box.y <= word.top <= box.y + box.height
        ):
            result.append(word.text)
    return " ".join(result)


def process_pdf(template: Template, pdf_path: str):
    pages = extract_page(pdf_path)

    model = {"template_name": template.name}

    for box in template.fields:
        value = extract_text(pages[box.page].words, box)
        for snt in box.sanities:
            value = sanity(snt, value)

        model.update({box.name: value})

    return model


template = Template(
    name="Rescisão",
    fields=[
        Box(name="cnpj",page=0,x=43,y=71,width=91,height=13,sanities=["replace:0001"]),
        Box(name="razao_social", page=0, x=140, y=71, width=209, height=13),
        Box(name="endereco", page=0, x=43, y=94, width=70, height=12),
        Box(name="cep", page=0, x=243, y=115, width=56, height=15),
        Box(name="bairro", page=0, x=401, y=94, width=76, height=12),
    ],
)

print(
    process_pdf(template, "/home/neves/Documentos/extractly/RESCISÃO DE CONTRATO.pdf")
)
