from src.database.database_config import DatabaseConfig
from src.database.database_service import DatabaseService
from src.entities.cliente import Cliente
from src.entities.result import Result, ResultCliente


class ClienteRepositorio:

    def __init__(self):
        self.database_service = DatabaseService()

    def salvar(self, cliente: Cliente) -> Result:
        return self.database_service.salvar_cliente(cliente)

    def buscar(self, id: int) -> ResultCliente:
        return self.database_service.buscar_cliente(id)
    
    def listar(self) -> ResultCliente:
        return self.database_service.listar_cliente()
    
    def delete(self, id: int) -> ResultCliente:
        return self.database_service.delete_cliente(id)
    
    def atualizar(self, id: int, cliente: Cliente) -> ResultCliente:
        return self.database_service.atualizar_cliente(id, cliente)