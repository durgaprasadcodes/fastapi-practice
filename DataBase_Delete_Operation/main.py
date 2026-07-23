from fastapi import FastAPI,HTTPException,status,Depends
from sqlalchemy.orm import Session
from database import get_db
from typing import Optional
import model
from pydantic import BaseModel,Field,EmailStr

app = FastAPI()

class User(BaseModel):
    name:str = Field(min_length=2)
    age:int = Field(ge = 18 , le = 100)
    mobile:str = Field(min_length=10, max_length=10)
    email:EmailStr
    
@app.get("/")
def get_user(db:Session = Depends(get_db)):
    return db.query(model.Users).all()

@app.post("/addUser",status_code=status.HTTP_201_CREATED)
def addUser(user:User,db:Session=Depends(get_db)):
    new_user = model.Users(
        name = user.name,
        age = user.age,
        mobile = user.mobile,
        email = user.email
    )
    db.add(new_user)
    try:
        db.commit()
    except:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Commiting Error")
    db.refresh(new_user)
    
    return {"message":"User Added Successfully"}

@app.delete("/deleteUser/{user_id}")
def deleteUser(user_id:int,db:Session=Depends(get_db)):
    user = db.query(model.Users).filter(model.Users.id == user_id).first()
    if not user:
        return {"message":"User Not Found"}
    db.delete(user)
    try:
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))
    
    return {"message":"User Deleted Succesfully"}
