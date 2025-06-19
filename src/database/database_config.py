
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.entities.result import Result, ResultCliente
from src.entities.favorito import Favorito
from src.entities.cliente import Cliente
from src.entities.produto import Produto
from src.database.database_models import Favoritos as FavoritosDatabase
from src.database.database_models import Cliente as ClienteDatabase
from src.usecases.produto.buscar_produto_id_usecase import BuscarProdutoIdUseCase
from http import HTTPStatus
import logging
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine



class DatabaseConfig:

    def __init__(self):

        self.connection_string = ("postgresql://admin:admin@localhost:5432/postgres")

        engine = create_engine(self.connection_string)

        with engine.connect() as connection:
            logging.info("Conexao estabelecida")

        Session = sessionmaker(bind=engine)
        self.session = Session()

    def salvar_cliente(self, cliente: Cliente) -> Result:
        try:

            cliente = ClienteDatabase(
                nome=cliente.nome, email=cliente.email, password=cliente.password)

            self.session.add(cliente)

            self.session.commit()

            result = Result(erro=False, mensagem="Cliente cadastrado com sucesso",
                            status_code=HTTPStatus.CREATED).format()
            return result

        except IntegrityError as e:
            if isinstance(e.orig, UniqueViolation):
                result = Result(erro=True, mensagem="Email já cadastrado",
                                status_code=HTTPStatus.OK).format()
            else:
                result = Result(
                    erro=True, mensagem=f"Erro inesperado do banco de dados - {e}", status_code=HTTPStatus.INTERNAL_SERVER_ERROR).format()
            self.session.rollback()
            return result
        finally:
            self.session.close()

    def buscar_cliente(self, id: int) -> ResultCliente:
        try:
            cliente = self.session.query(ClienteDatabase).filter_by(id=id).first()

            if cliente is None:
                result = ResultCliente(erro=False, mensagem="Cliente não encontrado",
                                       cliente=None, status_code=HTTPStatus.OK).format()
                return result

            favoritos = self.session.query(FavoritosDatabase).filter_by(user_id=id).all()

            if favoritos is None:
                cliente.favoritos = []
            else:
                cliente.favoritos = favoritos

            result = ResultCliente(erro=False, mensagem=None, cliente=cliente,
                                   status_code=HTTPStatus.OK).format()
            return result

        except Exception as e:
            result = ResultCliente(
                erro=True, mensagem=f"Erro inesperado do banco de dados - {e}", cliente=None, status_code=HTTPStatus.INTERNAL_SERVER_ERROR).format()
            return result
        finally:
            self.session.close()

    def listar_cliente(self) -> ResultCliente:
        try:
            clientes = self.session.query(ClienteDatabase).all()
            
            if len(clientes) == 0:
                result = ResultCliente(erro=False, mensagem="Não existem clientes cadastrados",
                                       cliente=None, status_code=HTTPStatus.OK).format()
                return result

            for cliente in clientes:
                favoritos = self.session.query(
                    FavoritosDatabase).filter_by(user_id=cliente.id).all()
                if favoritos is None:
                    cliente.favoritos = []
                else:
                    cliente.favoritos = favoritos

            result = ResultCliente(erro=False, mensagem=None, cliente=clientes,
                                   status_code=HTTPStatus.OK).format()
            return result

        except Exception as e:
            result = ResultCliente(
                erro=True, mensagem="Erro inesperado do banco de dados- {e}", cliente=None, status_code=HTTPStatus.INTERNAL_SERVER_ERROR).format()
            print(e)
            return result
        finally:
            self.session.close()

    def delete_cliente(self, id: int) -> ResultCliente:
        try:
            cliente = self.session.query(ClienteDatabase).filter_by(id=id).first()

            if cliente is None:
                result = ResultCliente(erro=False, mensagem="Cliente não encontrado",
                                       cliente=None, status_code=HTTPStatus.OK).format()
                return result

            favoritos = self.session.query(FavoritosDatabase).filter_by(user_id=id).all()

            if favoritos is not None:
                for favorito in favoritos:
                    self.session.delete(favorito)

                self.session.commit()

            self.session.delete(cliente)
            self.session.commit()

            result = ResultCliente(erro=False, mensagem="Cliente e seus Favoritos removido com sucesso",
                                   cliente=None, status_code=HTTPStatus.OK).format()
            return result

        except Exception as e:
            result = ResultCliente(
                erro=True, mensagem=f"Erro inesperado do banco de dados - {e}", cliente=None, status_code=HTTPStatus.INTERNAL_SERVER_ERROR).format()
            print(e)
            self.session.rollback()
            return result
        finally:
            self.session.close()

    def atualizar_cliente(self, id: int, novo_cliente: Cliente) -> ResultCliente:
        try:
            cliente = self.session.query(ClienteDatabase).filter_by(id=id).first()

            if cliente is None:
                result = ResultCliente(erro=False, mensagem="Cliente não encontrado",
                                       cliente=None, status_code=HTTPStatus.OK).format()
                return result

            favoritos = self.session.query(FavoritosDatabase).filter_by(user_id=id).all()

            print(favoritos)

            cliente.nome = novo_cliente.nome
            cliente.email = novo_cliente.email
            cliente.password = novo_cliente.password

            self.session.commit()

            result = ResultCliente(
                erro=False, mensagem="Cliente alterado com sucesso", cliente=None, status_code=HTTPStatus.OK).format()
            return result

        except Exception as e:
            result = ResultCliente(
                erro=True, mensagem="Erro inesperado do banco de dados", cliente=None, status_code=HTTPStatus.INTERNAL_SERVER_ERROR).format()
            print(e)
            self.session.rollback()
            return result
        finally:
            self.session.close()

    def salvar_favorito(self, favorito: Favorito) -> Result:
        try:

            buscar_produto_id_use_case = BuscarProdutoIdUseCase()

            produto: Produto = buscar_produto_id_use_case.execute(favorito.id_produto)
            cliente = self.session.query(ClienteDatabase).filter_by(id=favorito.user_id).first()

            if cliente is None:
                result = Result(erro=True, mensagem="Cliente não encontrado",
                                status_code=HTTPStatus.OK).format()
                return result

            if produto is None:
                result = Result(erro=True, mensagem="Produto não encontrado",
                                status_code=HTTPStatus.OK).format()
                return result

            favorito = FavoritosDatabase(id_produto=produto.id, titulo=produto.titulo, imagem=produto.imagemURL,
                                         preco=produto.preco, review=favorito.review, user_id=favorito.user_id)

            self.session.add(favorito)

            self.session.commit()

            result = Result(erro=False, mensagem="Favorito cadastrado com sucesso",
                            status_code=HTTPStatus.CREATED).format()
            return result

        except IntegrityError as e:
            if isinstance(e.orig, UniqueViolation):
                result = Result(erro=True, mensagem="Favorito já cadastrado",
                                status_code=HTTPStatus.INTERNAL_SERVER_ERROR).format()
            else:
                result = Result(erro=True, mensagem="Erro inesperado do banco de dados",
                                status_code=HTTPStatus.INTERNAL_SERVER_ERROR).format()
            self.session.rollback()
            return result
        finally:
            self.session.close()
