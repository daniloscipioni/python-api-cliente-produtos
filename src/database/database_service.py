from src.database.database_config import DatabaseConfig
from src.entities.cliente import Cliente
from src.entities.favorito import Favorito
from src.entities.result import Result, ResultCliente

class DatabaseService:
    def __init__(self):
        self.database_config = DatabaseConfig()

    def fechar_session(self):
        self.database_config.fechar()

    def salvar_cliente(self, cliente: Cliente) -> Result:
        return  self.database_config.salvar_cliente(cliente)

    def buscar_cliente(self, id: int) -> ResultCliente:
        return  self.database_config.buscar_cliente(id)
    
    def listar_cliente(self) -> ResultCliente:
        return  self.database_config.listar_cliente()
    
    def delete_cliente(self, id: int) -> ResultCliente:
        return  self.database_config.delete_cliente(id)
    
    def atualizar_cliente(self, id: int, cliente: Cliente) -> ResultCliente:
        return  self.database_config.atualizar_cliente(id, cliente)
    
    def salvar_favorito(self, favorito: Favorito) -> Result:
        return  self.database_config.salvar_favorito(favorito)


        
