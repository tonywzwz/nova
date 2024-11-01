from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from config.database import db

Base = declarative_base()

class Usuario (Base):
    #Definindo caracteristas da tabela no banco de dados.
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement= True)
    nome = Column(String(150))
    email = Column(String(150))
    senha = Column(String(150))

    #definindo caracteristica da classe.
    def _init_(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

#criando tabela no banco de dados.
Base.metadata.create_all(bind=db)