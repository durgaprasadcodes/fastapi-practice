from fastapi import FastAPI,HTTPException,status,File,UploadFile,Depends
from pydantic import BaseModel,Field,EmailStr
from database import get_db
from sqlalchemy.orm import Session
from typing import Optional
import model

app = FastAPI()

class BookType(BaseModel):
    title:str = Field(min_length=3)
    author:str = Field(min_length=3)
    date:str = Field(min_length=3)
    email:EmailStr
    
@app.get("/get_books")
def get_books(bookid:Optional[int] = 0 ,db:Session=Depends(get_db)):
    if bookid !=0 :
        return db.query(model.Book).filter(model.Book.id == bookid).first()
    return db.query(model.Book).all()


@app.get('/get_name')
def get_author(bookid:Optional[int] = 1 ,db:Session=Depends(get_db)):
    book = db.query(model.Book).filter(model.Book.id == bookid).first()
    if not book:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Book Not Found With That Index')
    return {f"Author At ID {bookid} ":f"{book.author}"}


@app.post('/post_book')
def post_book(book:BookType,db:Session=Depends(get_db)):
    new_book = model.Book(
        title = book.title,
        author = book.author,
        date = book.date,
        email = book.email
    )
    db.add(new_book)
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Commit Error')
    db.refresh(new_book)
    return {"Message":"Book Posted Successfully"}

