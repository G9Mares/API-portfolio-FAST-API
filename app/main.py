from fastapi import FastAPI, Depends, HTTPException, Request
import os

from sqlalchemy import Column
from utils.functions import validate_api_key, accepted_entity_body
import models.models as Models
from router import profile
from pydantic import ValidationError
import pandas as pd



app = FastAPI()
app.include_router(profile.router)

@app.get("/")
async def home():
    return {"Hellas":f"Men s World {os.getenv('MI_VARIABLE')}"}

@app.get('/{register}')
async def get_register(register:str, api_key:str = Depends(validate_api_key)):  
    if not hasattr(Models, register):
      raise HTTPException(status_code=404, detail=f'The entity {register} was not found')
    entity = getattr(Models, register)
    dependency = entity.dependency()
    a:Column = entity.__table__.columns
    for i in a:
        print(i.default)
        if i.foreign_keys:
            continue
        if i.primary_key:
            continue  

    if dependency:
      raise HTTPException(status_code=404, detail=f'The entity {register} depends on {dependency}')
    result = Models.session.query(entity).all()
    print(result)
    return result

@app.post('/{register}')
async def create_register(register:str,request:Request, api_key:str = Depends(validate_api_key)):
    if not hasattr(Models, register):
        raise HTTPException(status_code=404, detail=f'The entity {register} was not found')
    entity = getattr(Models, register)
    a:Column = entity.__table__.columns
    
    accept_body = entity.post_class()
    try:
        body = await request.json()
        for i in a:
            if i.foreign_keys:
                continue
            if i.primary_key:
                continue
            if not i.default:
                if i.name not in body:
                    raise HTTPException(status_code=422, detail=f'Miss the field {i.name}')
            
                
    except Exception as e:
        if type(e) != ValidationError:
            raise HTTPException(status_code=422, detail=f'The entity has a problem')
        raise HTTPException(status_code=422, detail=e.errors())
    
    response = entity.post_method(object_body)
    if type(response) == HTTPException:
      raise response
    
    return response
      
