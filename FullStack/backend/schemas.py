from pydantic import BaseModel,field_validator,EmailStr
import re

class Register(BaseModel):
    name:str 
    email:EmailStr
    password:str
    @classmethod
    @field_validator("password")
    def validate_pass(cls,value):
        if len(value)<8:
            raise ValueError("Password must be greater than 8 characters")
        if not re.search(value,r'[A-Z]'):
            raise ValueError("Password must contains atleast one uppercase letter")
        if not re.search(value,r'[a-z]'):
            raise ValueError("Password must contains atleast one lowercase letter")
        if not re.search(value,r'\d'):
            raise ValueError("Password must contains atleast one number ")
        if not re.search(value,r'[@!#$%^&*_-=+]'):
            raise ValueError("Password must contains atleast one Special letter")
        return value
            
class Login(BaseModel):
    email:EmailStr
    password:str
    
class Passwords:
    new_password:str
    old_password:str