from src.adaptadores.repositorio.produto_repositorio import ProdutoRepositorio
from src.entities.result import ResultProduto

class BuscarProdutosUseCase:
    def __init__(self):
        self.produto_repositorio = ProdutoRepositorio()
    
    def execute(self) -> list[ResultProduto]:
        return self.produto_repositorio.listar()