from src.entities.favorito import Favorito


class Cliente:
    def __init__(self, nome, email, password, favoritos:Favorito):
        self.nome = nome
        self.email = email
        self.password = password
        self.favoritos = favoritos
    
    def alterar_cliente(self, novo_nome, novo_email, novo_password):
        self.nome = novo_nome
        self.email = novo_email
        self.password = novo_password