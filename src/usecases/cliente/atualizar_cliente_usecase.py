from src.entities.cliente import Cliente
from src.adaptadores.repositorio.cliente_repositorio import ClienteRepositorio
from src.entities.result import Result

class AtualizarClienteUseCase:
    def __init__(self):
        self.cliente_repositorio = ClienteRepositorio()
    
    def execute(self, id:int, cliente: Cliente) -> Result:
        return self.cliente_repositorio.atualizar(id, cliente)