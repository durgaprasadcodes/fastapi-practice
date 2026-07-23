from database import get_db
from fastapi import FastAPI,HTTPException,status,Depends
from typing import Optional
from pydantic import BaseModel,EmailStr,Field
from slowapi import Limiter
from sqlalchemy.orm import Session
import model

# limiter = Limiter()
app = FastAPI()

class BookType(BaseModel):
    title:str = Field(min_length=3)
    author:str = Field(min_length=3)
    date:str
    email:EmailStr 
    
    
@app.get("/get_books")
async def get_Book(id:Optional[int]=0 ,db:Session = Depends(get_db)):
    if id !=0:
        return db.query(model.Book).filter(model.Book.id == id).first()
    return db.query(model.Book).all()

@app.post("/post_book")
async def post_Book(book:BookType,db:Session = Depends(get_db)):
    new_book = model.Book(
        title = book.title,
        author = book.author,
        date = book.date,
        email = book.email
    )
    db.add(new_book)
    try:
        db.commit()
    except :
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Commiting Error")
    db.refresh(new_book)
    return {"Message":"Book Posted Successfully"}

@app.put("/modify_book/{book_id}")    
async def modify_book(book_id:int = None,book:BookType = None,db:Session=Depends(get_db)):
    if not book_id:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book Index Not Found")
    if not book:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Incorrected Book Format")
    
    db_book = db.query(model.Book).filter(model.Book.id == book_id).first() 
    if not db_book:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book Not Found")
    db_book.title = book.title
    db_book.author = book.author
    db_book.date = book.date
    db_book.email = book.email
    db.add(db_book)
    try:
        db.commit()
    except:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Commiting Error")
    db.refresh(db_book)
    
    return {"message":"Book Modified Successfully"}
@app.delete('/delete_book/{book_id}')
async def delete_book(book_id:int,db:Session=Depends(get_db)):
    if not book_id :
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book Index Not Found")
    book = db.query(model.Book).filter(model.Book.id == book_id).first()
    if not book:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book  Not Found")
    db.delete(book)
    try:
        db.commit()
    except :
        db.rollback()
    
    return {"message":"Book Deleted Succesfully"}