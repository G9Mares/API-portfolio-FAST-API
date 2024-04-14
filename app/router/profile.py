from fastapi import APIRouter, Depends, HTTPException
import models.models as Models

from utils.functions import validate_api_key

router = APIRouter()
prefix = 'Profile'
router.prefix = "/"+prefix

@router.get('/{id_profile}/{register}')
async def get_register(register:str,id_profile:str, api_key:str = Depends(validate_api_key)):  
    if not hasattr(Models, register):
      raise HTTPException(status_code=404, detail=f'The entity {register} was not found')
    entity = getattr(Models, register)
    dependency = entity.dependency()
    print(dependency)
    if dependency != prefix:
      raise HTTPException(status_code=404, detail=f'The entity {register} depends on {dependency}')
    result = Models.session.query(entity).all()
    print(result)
    return result