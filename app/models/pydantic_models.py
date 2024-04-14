from pydantic import BaseModel


class Profile_body(BaseModel):
    full_name:str
    alias:str



