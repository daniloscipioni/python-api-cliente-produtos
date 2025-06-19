from fastapi import APIRouter,Response
from src.usecases.produto.buscar_produtos_usecase import BuscarProdutosUseCase
from src.usecases.produto.buscar_produto_id_usecase import BuscarProdutoIdUseCase
router = APIRouter(prefix="/produtos",tags=["Produtos"])

@router.get("/",
responses={
        200: {
            "description": "Sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "erro": False,
                        "mensagem": None,
                        "produtos": [
                                        {
                                        "id": 1,
                                        "titulo": "Fake Titulo",
                                        "preco": 109.95,
                                        "descricao": "Fake Descricao",
                                        "categoria": "Fake Categoria",
                                        "imagemURL": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg"
                                        },
                                    ],
                        "status_code": 200
                        }
                }
            }
        },
        500: {"description": "Internal server error"}
    })
def get(response: Response):
    buscar_produtos_use_case = BuscarProdutosUseCase()

    produtos = buscar_produtos_use_case.execute()

    response.status_code = produtos["status_code"]
    
    return produtos