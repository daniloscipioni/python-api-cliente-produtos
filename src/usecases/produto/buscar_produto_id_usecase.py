from src.entities.produto import Produto
from src.adaptadores.repositorio.produto_repositorio import ProdutoRepositorio
from src.entities.result import ResultProduto

class BuscarProdutoIdUseCase:
    def __init__(self):
        self.produto_repositorio = ProdutoRepositorio()
    
    def execute(self, id) -> Produto | None:
        return self.produto_repositorio.buscar_produto(id)