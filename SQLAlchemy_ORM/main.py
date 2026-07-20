from fastapi import FastAPI,Depends
from database import get_db,engine
from sqlalchemy.orm import Session
from pydantic import BaseModel
import model

app = FastAPI()

@app.get("/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(model.Book).filter(model.Book.id == book_id).first()

    if not book:
        return {"message": "Book not found"}

    return book

class BookType(BaseModel):
    title:str
    author:str
    publish_date:str
    
@app.post("/post")
def post_book(book: BookType, db: Session = Depends(get_db)):
    new_book = model.Book(
        title=book.title,
        author=book.author,
        publish_date=book.publish_date
    )

    db.add(new_book)

    try:
        db.commit()
        print("Commit successful")
    except Exception as e:
        print("Commit error:", e)
        db.rollback()
        raise


    return new_book