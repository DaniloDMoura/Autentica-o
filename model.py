import email
from sqlalchemy import Column, Integer, String
from orm import Base, engine

class Usuario(Base):


    __tablename__ = 'usuario'
    id = Column(Integer, primary_key = True)
    nome = Column(String(30), nullable = False, unique = True)
    email = Column(String(50), nullable = False, unique = True)
    senha_hash = Column(String(60), nullable = False)

Base.metadata.create_all(engine)