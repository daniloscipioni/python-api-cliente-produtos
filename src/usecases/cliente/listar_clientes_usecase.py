from src.entities.cliente import Cliente
from src.adaptadores.repositorio.cliente_repositorio import ClienteRepositorio
from src.entities.result import ResultCliente

class ListarClientesUseCase:
    def __init__(self):
        self.cliente_repositorio = ClienteRepositorio()
    
    def execute(self) -> ResultCliente:
        return self.cliente_repositorio.listar()