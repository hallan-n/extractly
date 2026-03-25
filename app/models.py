from dataclasses import dataclass

class Sanity:
    replace: str

@dataclass
class Box:
    name: str         # Nome do campo
    page: int         # Numero da página
    x: float          # Posição X em relação a página
    y: float          # Posição Y em relação a página
    width: float      # Largura da Box
    height: float     # Altura da Box
    sanity: list[str] # Lista de sanitys
 
@dataclass
class Template:
    name: str
    fields: list[Box]

@dataclass
class Word:
    text: str         # texto da palavra extraída
    x0: float         # posição horizontal inicial (esquerda)
    x1: float         # posição horizontal final (direita)
    top: float        # posição vertical do topo da palavra
    doctop: float     # topo relativo ao documento inteiro (não só a página)
    bottom: float     # posição vertical da base da palavra
    upright: bool     # se o texto está na orientação normal (não rotacionado)
    height: float     # altura da palavra (bottom - top)
    width: float      # largura da palavra (x1 - x0)
    direction: str    # direção do texto ("ltr" = esquerda→direita)

@dataclass
class Page:
    width: float      # Largura da página
    height: float     # Altura da página
    words: list[Word]