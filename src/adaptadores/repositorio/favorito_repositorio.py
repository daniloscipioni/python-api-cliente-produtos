from src.database.database_config import DatabaseConfig
from src.database.database_service import DatabaseService
from src.entities.favorito import Favorito
from src.entities.result import Result, ResultCliente


class FavoritoRepositorio:

    def __init__(self):
        self.database_service = DatabaseService()

    def salvar(self, favorito: Favorito) -> Result:
        return self.database_service.salvar_favorito(favorito)
