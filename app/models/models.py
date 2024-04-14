from uuid import uuid4
from fastapi import HTTPException
from sqlalchemy import ForeignKey, Column, String, Integer, CHAR, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker , attributes
import os
from dotenv import load_dotenv
import models.pydantic_models as PyModels
from sqlalchemy.exc import SQLAlchemyError, DatabaseError
from sqlalchemy.orm import relationship

load_dotenv()

Base = declarative_base()

db_name = "profile_db"
db_url = f'mysql+mysqlconnector://root:{os.getenv("MYSQL_ROOT_PASSWORD")}@{os.getenv("URL_SQL_SERVER")}/{db_name}'
engine = create_engine(db_url, echo=True)


Session = sessionmaker(bind=engine)
session = Session()



class Profile(Base):
    __tablename__ = "profile"
    id = Column(name="id",type_=String(120), primary_key=True)
    alias = Column(name="alias",type_=String(60))
    full_name = Column(name="full_name",type_=String(60))
    
    def dependency():
        return False
    
    def __init__(self,id:str,alias:str,full_name:str):
       print(type(alias), "-------------")
       self.id = id
       self.alias = alias
       self.full_name = full_name

    def post_class():
        return PyModels.Profile_body

    
    def post_method(request_body:PyModels.Profile_body):
        id = 'profile-'+str(uuid4())
        profile = Profile(id=id, alias=request_body.alias, full_name=request_body.full_name)
        same = session.query(Profile).filter_by(alias = request_body.alias).first()
        if same:
            return HTTPException(status_code=422, detail=f'The alias: {request_body.alias} is in use please choose other')
        try:
            session.add(profile)
            session.commit()
        except DatabaseError  as e:
            print(e._message(), "_message()") 
            return HTTPException(status_code=500, detail='An error ocurred when try to create profile try later')
        return {'message':f'Profile {request_body.alias} was created sucsesfully' }


    
class Info_profile(Base):
    __tablename__ = "info_profile"
    id = Column(name="id",type_=Integer, primary_key=True)
    language = Column(name="language",type_=String(60))
    about = Column(name="about",type_=String(500))
    tittle = Column(name="tittle",type_=String(100))
    profile = Column(String(60),ForeignKey(Profile.id) )
    profile_relashion = relationship('Profile', back_populates='info_profile')


    def dependency():
        return 'Profile'
    
    def __init__(self,id,firstname):
       self.id = id
       self.firstname = firstname

    def post_class():
        return 
    
    def post_method(args):
     pass

    
    
class Contact(Base):
    __tablename__ = "contact"
    id = Column(name="id",type_=Integer, primary_key=True)
    profile = Column(name="profile",type_=String(60))
    language = Column(name="language",type_=String(60))
    language = Column(name="label",type_=String(100))
    language = Column(name="icon",type_=String(60))
    language = Column(name="channel",type_=String(60))
    language = Column(name="tittle",type_=String(100))

    def dependency():
        return 'Profile'
    
    def __init__(self,id,firstname):
       self.id = id
       self.firstname = firstname

   

class Projects(Base):
    __tablename__ = "projects"
    id = Column(name="id",type_=Integer, primary_key=True)
    profile = Column(name="profile",type_=String(60))
    language = Column(name="language",type_=String(60))
    language = Column(name="tittle",type_=String(100))
    language = Column(name="description",type_=String(500))
    language = Column(name="url",type_=String(500))
    
    def __init__(self,id,firstname):
       self.id = id
       self.firstname = firstname

    def dependency():
        return 'Profile'

    


# print(dir(Base.metadata))
# print(dir(Person))