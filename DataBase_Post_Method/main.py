from fastapi import FastAPI,HTTPException,status,Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db,Base
import model

app = FastAPI()

class BookType(BaseModel):
    title:str
    author:str
    publish_date:str
    
@app.get("/{book_id}")
def get_books(book_id:int,db:Session = Depends(get_db)):
    book = db.query(model.Book).filter(model.Book.id == book_id).first()
    
    if not book:
        return {"message":"Book Not Found"}
    return book

@app.post('/post')
def post_book(book:BookType ,db:Session = Depends(get_db)):
    new_book  = model.Book(
        title = book.title,
        author = book.author,
        publish_date = book.publish_date
    )  
    db.add(new_book)
    try:
        db.commit()
        print("Commit Successful")
    except Exception as e:
        print("Commit Error :",e)
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Commit Error")
    return new_book
    

