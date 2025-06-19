from src.entities.cliente import Cliente
from src.adaptadores.repositorio.cliente_repositorio import ClienteRepositorio
from src.entities.result import Result

class DeleteClienteUseCase:
    def __init__(self):
        self.cliente_repositorio = ClienteRepositorio()
    
    def execute(self, id: int) -> Result:
        return self.cliente_repositorio.delete(id)