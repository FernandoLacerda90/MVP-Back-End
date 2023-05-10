
from sqlalchemy import Column, String, Integer, DateTime, Float
from  model import Base
from typing import Union

class Produto(Base):
    __tablename__ = 'produto'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    descricao = Column(String)
    preco_venda = Column(Float)
    preco_compra = Column(Float)
    estoque = Column(Integer)
    data_criacao = Column(DateTime)
    data_atualizacao = Column(DateTime)
    
    def __init__(self, nome:str, descricao:str, preco_venda:float,preco_compra:float,
                 estoque:int,
                 data_criacao:Union[DateTime, None] = None):
        
        self.nome = nome
        self.descricao = descricao
        self.preco_venda = preco_venda
        self.preco_compra = preco_compra
        self.estoque = estoque
        
        if data_criacao:
            self.data_criacao = data_criacao
    