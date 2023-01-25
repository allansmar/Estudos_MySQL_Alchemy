import sqlalchemy as db
import pymysql

# Fazendo conexão com banco de dados -> 'aula409'
# db = apelido da biblio sqlalchemy; SINTAXE -> var = db.create_engine("driver://usuário:senha@servidor:porta/database")
engine = db.create_engine("mysql+pymysql://root:@localhost:3306/aula409")

# Importando coisas do SQL Alchemy / Criando modelo
from sqlalchemy.orm import (declarative_base, sessionmaker)
from sqlalchemy import Column, Integer, String, Float
Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produtos'
    idproduto = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(60))
    valor = Column(Float)

# Criando tabela no banco de dados
Base.metadata.create_all(engine)

# Criação das Sessões de Conexão com o banco
Session = sessionmaker(bind=engine)
session = Session()

# Inserindo Dados com base na Classe
produto1 = Produto(nome="Detergente", valor=2.09)
produto2 = Produto(nome="Amendoim", valor=5)
produto3 = Produto(nome="Coca-Cola", valor=10)
produto4 = Produto(nome="Chocolate", valor=4.99)
produto5 = Produto(nome="Pilha", valor=10)

# Inserindo o objeto no Banco de Dados
# session.add_all([produto1, produto2, produto3, produto4, produto5])

# Para inserir mais de um objeto, utiliza-se o session.add_all
# session.add_all([produto1, produto2, produto3, produto5, produto4])

# Confirmar as inserções
session.commit()

# Consultas
# Geral
print("GERAL")
produtos = session.query(Produto).all()
for prod in produtos:
    print(f'{prod.nome} \tR$ {prod.valor}')
print('===========================================')

# 1 Quais as características do prod DETERGENTE?
produtos = session.query(Produto).all()
for prod in produtos:
    if prod.nome == 'Detergente':
        print(f'{prod.nome} \tR$ {prod.valor}')
print('===========================================')

# 2 Verificar se existe na tabela uma lista de dois produtos passadas por voce (Ex: ["Detergente","Bola"])

# 3 Retornar os itens onde o valor seja maior ou igual a 5:
print('valor seja maior ou igual a 5')
produtos = session.query(Produto).all()
for prod in produtos:
    if prod.valor >= 5:
        print(f'{prod.nome} \tR$ {prod.valor}')

# 4 Verifique os itens onde o nome seja Amendoim OU Detergente.
from sqlalchemy import or_
produtos = session.query(Produto).filter(or_(Produto.nome == "Amendoim", Produto.nome == "Detergente"))
for t in produtos:
    print(t.nome)