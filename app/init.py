import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import uvicorn
import models.models as Models
from models.utils_models import update_models
from sqlalchemy_utils import database_exists, create_database




load_dotenv()
if __name__ == "__main__":
    cargar_modelos = input("Deseas cargar los modelos?...[y/n]\n")
    if cargar_modelos in ['y', 'Y']:
        ## Here you can configurate your own engine or you could use a mysql docker, only need to set your .env
        if not database_exists(Models.engine.url):
            create_database(Models.engine.url)
        Models.Base.metadata.create_all(Models.engine)
        #update_models(engine=engine)

    run_uvicorn = input("Quieres levantar el servidor?...[y/n]\n")
    if run_uvicorn in ['y', 'Y']:
        uvicorn.run(app="main:app", reload=True, port=80, host="0.0.0.0")