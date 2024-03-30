from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()

class Person(Base):
    __tablename__ = "Persons"
    id = Column(name="id",type_=Integer, primary_key=True)
    firstname = Column(name="firstname",type_=String)
    
    def __init__(self,id,firstname):
       self.id = id
       self.firstname = firstname

    def __repr__(self):
        return f" i dont care"
    
## Here you can configurate your own engine or you could use a mysql docker, only need to set your .env


db_url = f'mysql+mysqlconnector://root:{os.getenv("MYSQL_ROOT_PASSWORD")}@localhost:3307'
engine = create_engine(db_url)
Base.metadata.create_all(bind =engine)