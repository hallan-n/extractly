# Extractly

Extractly é uma ferramenta para extração de dados estruturados de arquivos PDF. Utiliza templates definidos por caixas delimitadoras (bounding boxes) para identificar regiões de texto em páginas específicas, aplicando funções de "sanity" para limpeza e validação dos dados extraídos.

## Funcionalidades

- **Interface Web**: Upload de PDFs e definição visual de áreas de extração através de retângulos desenhados nas páginas.
- **API Backend**: Processamento de PDFs via FastAPI, retornando dados estruturados baseados em templates.
- **Sanity Checks**: Diversas funções para limpar e extrair dados específicos, como CNPJ, CPF, datas, CEPs, etc.
- **Suporte a Templates**: Definição de templates com múltiplos campos, cada um associado a uma página e coordenadas.

## Tecnologias Utilizadas

- **Backend**: FastAPI (Python)
- **Processamento de PDF**: pdfplumber, pdfminer.six, pypdfium2
- **Frontend**: HTML, JavaScript, Tailwind CSS, PDF.js
- **Validação**: Pydantic para modelos de dados

## Instalação

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd extractly
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o servidor:
   ```bash
   python app/main.py
   ```

   O servidor estará disponível em `http://localhost:8000`.

## Uso

### Interface Web

1. Abra `index.html` no navegador.
2. Faça upload de um arquivo PDF.
3. Desenhe retângulos nas áreas de interesse em cada página.
4. Defina labels e funções de sanity para cada campo.
5. Use o botão "LOG RETÂNGULOS" para visualizar o template gerado.

### API

Envie uma requisição POST para `/` com:
- `template`: JSON string representando o template (Template model).
- `file`: Arquivo PDF.

Exemplo de resposta:
```json
{
  "template_name": "Nome do Template",
  "campo1": "valor extraído",
  "campo2": "valor processado"
}
```

## Modelos de Dados

- **Box**: Define uma área de extração com nome, página, coordenadas e sanities.
- **Template**: Contém nome e lista de Boxes.
- **Word**: Representa uma palavra extraída com posições.
- **Page**: Página com largura, altura e lista de Words.

## Funções de Sanity

Incluem limpeza de texto, extração de padrões específicos (datas, documentos, etc.) e validações.

Exemplos:
- `get_cnpj`: Extrai CNPJ do texto.
- `until:texto`: Remove tudo após "texto".
- `replace:old`: Substitui "old" por vazio.

## Contribuição

Contribuições são bem-vindas! Abra issues ou pull requests no repositório.

## Licença

[Adicione licença aqui]