import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from fastapi import APIRouter,Response
from pydantic import BaseModel
from src.database.validacao.favorito import Favorito
from src.usecases.favorito.criar_favorito_usecase import CriarFavoritoUseCase
router = APIRouter(prefix="/favorito",tags=["Favoritos"])

@router.post("/",
responses={
        200: {
            "description": "Sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "erro": True,
                        "mensagem": "Cliente não encontrado",
                        "status_code": 200
                        }
                }
            }
        },
        201: {
            "description": "Sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "erro": False,
                        "mensagem": "Favorito cadastrado com sucesso",
                        "status_code": 201
                        }
                }
            }
        },
        500: {"description": "Internal server error"}
    })
def adicionar(favorito: Favorito, response: Response):
    criar_favorito_use_case = CriarFavoritoUseCase()

    favorito = criar_favorito_use_case.execute(favorito)
    
    response.status_code = favorito["status_code"]

    return favorito
