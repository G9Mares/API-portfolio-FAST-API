from fastapi import Header, HTTPException
import inspect

def validate_api_key(api_key:str = Header(...)):
    ## 3312 primero devolver registros y despues crear un mecanismo de seguridad
    print(api_key)
    return True

def accepted_entity_body(object):
    args = inspect.signature(object)