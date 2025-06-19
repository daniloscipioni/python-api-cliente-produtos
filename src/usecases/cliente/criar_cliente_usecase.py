from src.entities.cliente import Cliente
from src.adaptadores.repositorio.cliente_repositorio import ClienteRepositorio
from src.entities.result import Result

class CriarClienteUseCase:
    def __init__(self):
        self.cliente_repositorio = ClienteRepositorio()
    
    def execute(self, cliente: Cliente) -> Result:
        return self.cliente_repositorio.salvar(cliente)