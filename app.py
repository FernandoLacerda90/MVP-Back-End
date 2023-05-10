from fastapi import FastAPI
from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError
from model import Session, Produto
from logger import logger
from schema.error import ErrorSchema
from schema.produto import ListagemProdutosSchema, ProdutoBuscaSchema, ProdutoDelSchema, ProdutoSchema, ProdutoViewSchema, apresenta_produto, apresenta_produtos
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


origins = [
    "*",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/produto')
def add_produto(form: ProdutoSchema):
    produto = Produto(
        nome=form.nome,
        descricao=form.descricao,
        estoque=form.estoque,
        preco_venda=form.preco_venda,
        preco_compra=form.preco_compra)
    
    logger.debug(f"Adicionando produto de nome: '{produto.nome}'")

    try:
        # criando conexão com a base
        session = Session()
        # adicionando produto
        session.add(produto)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado produto de nome: '{produto.nome}'")
        return apresenta_produto(produto), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Produto de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"message": error_msg}, 400


@app.get('/produtos', description="Lista Todos os Produtos", summary="Lista Produtos")
def get_produtos():
    """Faz a busca por todos os Produto cadastrados
    Retorna uma representação da listagem de produtos.
    """
    logger.debug(f"Coletando produtos ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    produtos = session.query(Produto).all()
    if not produtos:
        # se não há produtos cadastrados
        return {"produtos": []}, 200
    else:
        logger.debug(f"%d rodutos econtrados" % len(produtos))
        # retorna a representação de produto
        print(produtos)
        return apresenta_produtos(produtos), 200


@app.get('/produto')
def get_produto(id: str = None):
    """Faz a busca por um Produto a partir do id do produto
    Retorna uma representação dos produtos e comentários associados.
    """
    produto_id = int(id)
    logger.debug(f"Coletando dados sobre produto #{produto_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    produto = session.query(Produto).filter(Produto.id == produto_id).first()
    if not produto:
        # se o produto não foi encontrado
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{produto_id}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Produto econtrado: '{produto.nome}'")
        # retorna a representação de produto
        return apresenta_produto(produto), 200


@app.delete('/produto')
def del_produto(query: ProdutoBuscaSchema):
    """Deleta um Produto a partir do nome de produto informado
    Retorna uma mensagem de confirmação da remoção.
    """
    produto_id = query.id
    print(produto_id)
    logger.debug(f"Deletando dados sobre produto #{produto_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Produto).filter(Produto.id == produto_id).delete()
    session.commit()
    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado produto #{produto_id}")
        return {"message": "Produto removido", "id": produto_id}
    else:
        # se o produto não foi encontrado
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao deletar produto #'{produto_id}', {error_msg}")
        return {"message": error_msg}, 404