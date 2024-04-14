import models.models as Models
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy import MetaData, Table
from models.models import engine
from sqlalchemy.orm import sessionmaker , attributes




def update_models(engine, model:str = "all",):

    meta = MetaData()
    meta.reflect(bind=engine)
    tables = meta.tables
    ## This part is if the model = all
    for i in dir(Models):
        model_class =getattr(Models, i)  
        if type(model_class) !=DeclarativeMeta:
          continue
        
        if not hasattr(model_class ,"__tablename__"):
            continue

        table_name =  getattr(model_class, "__tablename__")
        if table_name not in  tables:
            continue
        real_columns = tables[table_name].columns
        table_model = getattr(model_class, "__table__")
        model_columns = table_model.columns
        print(model_columns, "Those are real ---->", real_columns )