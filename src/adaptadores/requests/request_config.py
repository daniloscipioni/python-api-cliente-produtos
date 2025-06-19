
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import requests
from src.entities.produto import Produto
from src.database.database_models import Cliente as ClienteDatabase
from src.database.database_models import Favoritos as FavoritosDatabase
from http import HTTPStatus
from src.entities.result import ResultProduto

class RequestConfig:
    
    def __init__(self):
        self.url_produtos = ("https://fakestoreapi.com/products")
        

    def buscar_produtos(self) -> ResultProduto:
        try:
            produtos = requests.get(f"{self.url_produtos}").json()
            lista_produtos = []
            
            for produto in produtos:
                produto = Produto(
                                    id=produto["id"],
                                    titulo=produto["title"],
                                    categoria=produto["category"],
                                    descricao=produto["description"],
                                    imagemURL=produto["image"],
                                    preco=produto["price"])
                lista_produtos.append(produto)
                
            return ResultProduto(erro=False,mensagem=None, produto=lista_produtos, status_code=HTTPStatus.OK).format()
            
        except Exception as e:
            return ResultProduto(erro=True,mensagem=f"Erro inesperado do banco de dados - {e}", produto=None, status_code=HTTPStatus.INTERNAL_SERVER_ERROR).format()
    
    def buscar_produtos_id(self, id) -> Produto | None:
        try:
            
            produto_request = requests.get(f"{self.url_produtos}/{id}")
            
            
            if produto_request.content:
                produto = requests.get(f"{self.url_produtos}/{id}").json()

                produto = Produto(
                                id=produto["id"],
                                titulo=produto["title"],
                                categoria=produto["category"],
                                descricao=produto["description"],
                                imagemURL=produto["image"],
                                preco=produto["price"])
                    
                return produto

            return None
            
        except Exception as e:
            return ResultProduto(erro=True,mensagem="Erro inesperado do banco de dados", produto=None).format()



    
                                  