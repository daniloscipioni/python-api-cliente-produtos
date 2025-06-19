from typing import Optional
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class Cliente(Base):
    __tablename__ = "tbl_cliente"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    password:Mapped[str] = mapped_column(String, deferred=True)
    __table_args__ = (UniqueConstraint("email", name="model_email_key"),)

    
    def __repr__(self) -> str:
        return f"Cliente(id={self.id!r}, nome={self.nome!r}, email={self.email!r})"

class Favoritos(Base):
    __tablename__ = "tbl_favoritos"
    id: Mapped[int] = mapped_column(primary_key=True)
    id_produto: Mapped[int] 
    titulo: Mapped[str]
    imagem: Mapped[str]
    preco:  Mapped[float]
    review:  Mapped[Optional[str]] = mapped_column(String,)
    user_id: Mapped[int] = mapped_column(ForeignKey("tbl_cliente.id"), deferred=True)
    __table_args__ = (UniqueConstraint("id_produto","user_id", name="model_id_produto_key"),)


    def __repr__(self) -> str:
        return f"Favoritos(id={self.id!r}, titulo={self.titulo!r}, imagem={self.imagem!r}, preco={self.preco!r}, review={self.review!r})"

