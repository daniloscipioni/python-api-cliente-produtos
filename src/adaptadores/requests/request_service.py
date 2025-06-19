from src.adaptadores.requests.request_config import RequestConfig
from src.entities.result import ResultProduto
from src.entities.produto import Produto

class RequestService:
    def __init__(self):
        self.request_config = RequestConfig()

    def listar_produtos(self) -> ResultProduto:
        return self.request_config.buscar_produtos()
    
    def buscar_produto(self, id) -> Produto | None:
        return self.request_config.buscar_produtos_id(id)
