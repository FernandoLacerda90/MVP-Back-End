from typing import Optional, List
from pydantic import BaseModel
from model.produto import Produto


class ProdutoSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    id: int = None
    nome: str = None
    descricao: str = None
    estoque: Optional[int] = None
    preco_venda: float = None
    preco_compra: float = None


class ProdutoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    id: int = 1


class ListagemProdutosSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    produtos: List[ProdutoSchema]


def apresenta_produtos(produtos: List[Produto]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for produto in produtos:
        result.append({
            "id": produto.id,
            "nome": produto.nome,
            "descricao": produto.descricao,
            "estoque": produto.estoque,
            "preco_venda": produto.preco_venda,
            "preco_compra": produto.preco_compra,
        })

    return {"produtos": result}


class ProdutoViewSchema(BaseModel):
    """ Define como um produto será retornado: produto.
    """
    id: int = 1
    nome: str = "Coca-Cola 2L"
    descricao: str = "Refrigerante Coca-Cola 2L"
    estoque: Optional[int] = 12
    preco_venda: float = 12.50
    preco_compra: float = 5.00


class ProdutoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    id: int


def apresenta_produto(produto: Produto):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": produto.id,
        "nome": produto.nome,
        "descricao": produto.descricao,
        "estoque": produto.estoque,
        "preco_venda": produto.preco_venda,
        "preco_compra": produto.preco_compra,
    }