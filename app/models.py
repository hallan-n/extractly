from pydantic import BaseModel


class Box(BaseModel):
    name:  str  # Nome do campo
    page: int  # Numero da página
    x: float  # Posição X em relação a página
    y: float  # Posição Y em relação a página
    width: float  # Largura da Box
    height: float  # Altura da Box
    sanities: list[str] = []  # Lista de sanitys


class Template(BaseModel):
    name: str
    fields: list[Box]


class Word(BaseModel):
    text: str  # texto da palavra extraída
    x0: float  # posição horizontal inicial (esquerda)
    x1: float  # posição horizontal final (direita)
    top: float  # posição vertical do topo da palavra
    doctop: float  # topo relativo ao documento inteiro (não só a página)
    bottom: float  # posição vertical da base da palavra
    upright: bool  # se o texto está na orientação normal (não rotacionado)
    height: float  # altura da palavra (bottom - top)
    width: float  # largura da palavra (x1 - x0)
    direction: str  # direção do texto ("ltr" = esquerda→direita)


class Page(BaseModel):
    width: float  # Largura da página
    height: float  # Altura da página
    words: list[Word]


# print(Template(
#     name="Rescisão",
#     fields=[
#         Box(name="cnpj", page=0, x=43, y=71, width=91, height=13, sanities=["get_int:3", "until:1"]),
#         Box(name="razao_social", page=0, x=140, y=71, width=209, height=13),
#         Box(name="endereco", page=0, x=43, y=94, width=70, height=12),
#         Box(name="cep", page=0, x=243, y=115, width=56, height=15),
#         Box(name="bairro", page=0, x=401, y=94, width=76, height=12),
#     ],
# ).dict())
