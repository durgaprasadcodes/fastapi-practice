from pydantic import EmailStr ,BaseModel ,Field
from typing import Union


class UserInSignUp(BaseModel):
    name : str 
    email : EmailStr
    password : str = Field(min_length=8)
    
class UserOutPut(BaseModel):
    id : int
    name : str 
    email : EmailStr
    
class UserInUpdate(BaseModel):
    id : int
    name : Union[str,None] = None
    email : Union[EmailStr,None] = None
    password : Union[str,None] = None
    
class UserInLogin(BaseModel):
    email : str
    password : str
    
class UserWithToken(BaseModel):
    token : str
    