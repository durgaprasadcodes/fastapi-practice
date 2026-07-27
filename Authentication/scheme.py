from pydantic import BaseModel,EmailStr,Field

class UserDetails(BaseModel):
    name:str = Field(min_length=100)
    email:str = EmailStr
    password:str = Field(max_length=20)