from pydantic import EmailStr ,BaseModel ,Field,field_validator
from typing import Union
import re


class UserInSignUp(BaseModel):
    name : str 
    email : EmailStr
    password:str = Field(min_length=8,description="Password must be at least 8 characters long.")
    @field_validator("password")
    @classmethod
    def validate_pasword(cls, value):
        if not re.search(r"[A-Z]",value):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not re.search(r"[a-z]",value):
            raise ValueError("Password must contain at least one lowercase letter.")
        if not re.search(r"\d",value):
            raise ValueError("Password must contain at least one digit.")
        return value
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
    email : EmailStr
    password : str
    
class UserWithToken(BaseModel):
    token : str
    