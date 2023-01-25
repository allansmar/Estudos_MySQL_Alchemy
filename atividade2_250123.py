# Importando bibliotecas
import sqlalchemy as db
import pymysql

# Conexao com banco de dados | SINTAXE -> var = db.create_engine("driver://usuário:senha@servidor:porta/database")
engine = db.create_engine("mysql+pymysql://root:@localhost:3306/aula409")

# Importando coisas do mysql
from sqlalchemy.orm import (declarative_base, sessionmaker)
from sqlalchemy import Column, Integer, String, Float
Base = declarative_base()

# Criando modelo
class Artista(Base):
    __tablename__ = 'artistas'
    idartista = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(60))
    estilo = Column(String(60))
    integrantes = Column(String(60))
    pais = Column(String(60))

# Criando a sessão
Session = sessionmaker(bind=engine)
session = Session()

# Adicionando dados
artista1 = Artista(nome="Engenheiros do Havaí",estilo="Rock Nacional",integrantes="Humberto Gessinger e banda", pais="Brasil")
artista2 = Artista(nome="Chambinho do Acordeon",estilo="Forró",integrantes= "Chambinho", pais="Brasil")
artista3 = Artista(nome="Red Hot Chilli Peppers",estilo="Rock internacional",integrantes= "Flear",pais="Internacional")

session.add_all([artista1, artista2, artista3])

# Criando tabela no banco de dados
Base.metadata.create_all(engine)

session.commit()