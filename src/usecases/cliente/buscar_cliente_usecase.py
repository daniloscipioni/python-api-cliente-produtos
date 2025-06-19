from src.entities.cliente import Cliente
from src.adaptadores.repositorio.cliente_repositorio import ClienteRepositorio
from src.entities.result import ResultCliente

class BuscarClienteUseCase:
    def __init__(self):
        self.cliente_repositorio = ClienteRepositorio()
    
    def execute(self, id: int) -> ResultCliente:
        return self.cliente_repositorio.buscar(id)