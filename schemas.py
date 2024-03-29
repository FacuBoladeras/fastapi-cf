from pydantic import BaseModel
from pydantic import validator


class UserRequestModel(BaseModel):
    username: str
    password: str
    
    @validator("username")
    def username_validator(cls, username):
        if len(username) < 3 or len(username) >50:
            raise ValueError(" La longitud debe encontrarse entre 3 y 50 caracteres")
        else:
            return username
        
class UserResponseModel(BaseModel):
    
    id: int
    username: str