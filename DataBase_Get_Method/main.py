from fastapi import FastAPI,status,HTTPException ,Depends
from database import engine,get_db
from pydantic import BaseModel
from sqlalchemy.orm import Session
import model


app = FastAPI()

class BookType(BaseModel):
    title:str
    author:str
    published_date:str

@app.get("/getAllBooks")
def getBook(db:Session=Depends(get_db)):
    return db.query(model.Book).all()

@app.get("/getBookByID/{id}")
def getBookById(id:int,db:Session=Depends(get_db)):
    return db.query(model.Book).filter(model.Book.id == id).first()

@app.get('/getName/{id}')
def getName(id:int,db:Session=Depends(get_db)):
    book= db.query(model.Book).filter(model.Book.id == id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"title":book.title}

    
@app.post("/postBook")
def postBook(book:BookType,db:Session=Depends(get_db)):
    new_book = model.Book(
        title =  book.title,
        author = book.author,
        published_date = book.published_date 
    )
    db.add(new_book)
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book Not Found")
    
    return {"message":"Book Posted Successfully"}


    