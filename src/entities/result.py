from src.entities.produto import Produto
from src.entities.cliente import Cliente


class Result:
    def __init__(self, erro:bool, mensagem:str, status_code: int):
        self.erro = erro
        self.mensagem = mensagem
        self.status_code = status_code

    def format(self):
        return {"erro":self.erro, "mensagem":self.mensagem, "status_code":self.status_code}

class ResultCliente:
    def __init__(self, erro:bool, mensagem:str, cliente: Cliente, status_code: int):
        self.erro = erro
        self.mensagem = mensagem
        self.cliente = cliente
        self.status_code = status_code

    def format(self):
        return {"erro":self.erro, "mensagem":self.mensagem, "cliente": self.cliente, "status_code":self.status_code}

class ResultProduto:
    def __init__(self, erro:bool, mensagem:str, produto: list[Produto], status_code: int):
        self.erro = erro
        self.mensagem = mensagem
        self.produto = produto
        self.status_code = status_code

    def format(self):
        return {"erro":self.erro, "mensagem":self.mensagem, "produtos": self.produto, "status_code":self.status_code }