from pydantic import BaseModel
from http import HTTPStatus
from src.database.validacao.cliente import Cliente
from src.usecases.cliente.buscar_cliente_usecase import BuscarClienteUseCase
from src.usecases.cliente.criar_cliente_usecase import CriarClienteUseCase
from src.usecases.cliente.delete_cliente_usecase import DeleteClienteUseCase
from src.usecases.cliente.atualizar_cliente_usecase import AtualizarClienteUseCase
from src.usecases.cliente.listar_clientes_usecase import ListarClientesUseCase
from fastapi import APIRouter, Response
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


router = APIRouter(prefix="/cliente", tags=["Cliente"])


@router.post("/",
    responses={
        200: {
            "description": "Sucesso",
            "content": {
                "application/json": {
                    "example": {"erro": True, "mensagem": "Email já cadastrado", "status_code": 200}
                }
            }
        },
        201: {
            "description": "Cliente cadastrado com sucesso",
            "content": {
                "application/json": {
                    "example": {"erro": False, "mensagem": "Cliente cadastrado com sucesso", "status_code": 201}
                }
            }
        },
        500: {"description": "Internal server error"}
    })
def adicionar(cliente: Cliente, response: Response):

    criar_cliente_use_case = CriarClienteUseCase()

    cliente = criar_cliente_use_case.execute(cliente)

    response.status_code = cliente["status_code"]

    return cliente


@router.get("/{id}",
responses={
        200: {
            "description": "Sucesso",
            "content": {
                "application/json": {
                    "example": {
                         "erro": False,
                         "mensagem": None,
                        "cliente": 
                            {
                            "email": "fake@gmail.com.br",
                            "nome": "Fake Name",
                            "id": 3,
                            "favoritos": [
                                {
                                "imagem": "https://fakestoreapi.com/img/81QpkIctqPL._AC_SX679_.jpg",
                                "id": 1,
                                "review": "Fake Review",
                                "preco": 599,
                                "id_produto": 13,
                                "titulo": "Fake Titulo"
                                }
                            ]
                            },
                        "status_code": 200
                        }
                }
            }
        },
        500: {"description": "Internal server error"}
    })
def buscar(id, response: Response):
    buscar_cliente_use_case = BuscarClienteUseCase()

    cliente = buscar_cliente_use_case.execute(id)

    response.status_code = cliente["status_code"]

    return cliente


@ router.get("/",
responses={
        200: {
            "description": "Sucesso",
            "content": {
                "application/json": {
                    "example": {
                         "erro": False,
                         "mensagem": None,
                         "cliente": [
                            {
                            "email": "fake@gmail.com.br",
                            "nome": "Fake Name",
                            "id": 3,
                            "favoritos": [
                                {
                                "imagem": "https://fakestoreapi.com/img/81QpkIctqPL._AC_SX679_.jpg",
                                "id": 1,
                                "review": "Fake Review",
                                "preco": 599,
                                "id_produto": 13,
                                "titulo": "Fake Titulo"
                                }
                            ]
                            },
                        ],
                        "status_code": 200
                        }
                }
            }
        },
        500: {"description": "Internal server error"}
    })
def listar(response: Response):
    listar_cliente_use_case = ListarClientesUseCase()

    cliente = listar_cliente_use_case.execute()

    response.status_code = cliente["status_code"]

    return cliente


@ router.delete("/{id}",
responses={
        200: {
            "description": "Sucesso",
            "content": {
                "application/json": {
                    "example": {
                            "erro": False,
                            "mensagem": "Cliente e seus Favoritos removido com sucesso",
                            "cliente": None,
                            "status_code": 200
                             }
                }
            }
        },
        500: {"description": "Internal server error"}
    })
def delete(id, response: Response):

    delete_cliente_use_case = DeleteClienteUseCase()

    delete_cliente = delete_cliente_use_case.execute(id)

    response.status_code = delete_cliente["status_code"]

    return delete_cliente


@ router.patch("/{id}",
responses={
        200: {
            "description": "Sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "erro": False,
                        "mensagem": "Cliente alterado com sucesso",
                        "cliente": None,
                        "status_code": 200
                        }
                }
            }
        },
        500: {"description": "Internal server error"}
    })
def atualizar(id, cliente: Cliente, response: Response):

    atualizar_cliente_use_case = AtualizarClienteUseCase()

    cliente = atualizar_cliente_use_case.execute(id, cliente=cliente)

    response.status_code = cliente["status_code"]

    return cliente
