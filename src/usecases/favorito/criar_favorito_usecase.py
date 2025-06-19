from src.entities.favorito import Favorito
from src.adaptadores.repositorio.favorito_repositorio import FavoritoRepositorio
from src.entities.result import Result

class CriarFavoritoUseCase:
    def __init__(self):
        self.favorito_repositorio = FavoritoRepositorio()
    
    def execute(self, favorito: Favorito) -> Result:
        return self.favorito_repositorio.salvar(favorito)