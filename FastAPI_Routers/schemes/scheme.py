from pydantic import BaseModel,EmailStr,Field

class UserInLogin(BaseModel):
    email:EmailStr
    password:str = Field(min_length=8)
    
class UserInSignUp(BaseModel):
    name:str
    email:EmailStr
    password:str
    