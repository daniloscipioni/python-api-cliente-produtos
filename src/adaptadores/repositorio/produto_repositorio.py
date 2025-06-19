from src.adaptadores.requests.request_service import RequestService
from src.entities.cliente import Cliente
from src.entities.result import ResultProduto
from src.entities.produto import Produto

class ProdutoRepositorio:

    def __init__(self):
        self.request_service = RequestService()
 
    def listar(self) -> ResultProduto:
        return self.request_service.listar_produtos()
    
    def buscar_produto(self, id)-> Produto | None:
        return self.request_service.buscar_produto(id)