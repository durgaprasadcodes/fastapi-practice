from fastapi import FastAPI,HTTPException,status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Atomic Habits",
        "author": "James Clear",
        "pages": 320
    },
    {
        "id": 2,
        "title": "Deep Work",
        "author": "Cal Newport",
        "pages": 304
    },
    {
        "id": 3,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt",
        "pages": 352
    },
    {
        "id": 4,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "pages": 464
    },
    {
        "id": 5,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "pages": 544
    }
]

@app.get("/")
async def get_books():
  return books

@app.get("/greet")
async def greet(name:Optional[str]="User",age:Optional[int]=None):
  return {"message" : f"Mr.{name} you are {age} old"}

class Book(BaseModel):
  id:int
  title:str
  author:str
  pages:int
  
@app.post("/post_book")
async def postBook(book:Book):
  books.append(book)
  return {
    "id":book.id,
    "title":book.title,
    "author":book.author,
    "pages":book.pages
  }

@app.put("/update/{id}")
async def update(id:int ,book:Book):
  for bk in books:
    if bk["id"] == id:
      bk["id"] = book.id
      bk["title"] = book.title
      bk["author"] = book.author
      bk["pages"] = book.pages
      return {"message" : "Book Updated Succefully"}
  return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book Not Found")

@app.delete("/deletepost/{id}")
async def delete(id:int):
  for book in books:
    if book["id"] == id:
      books.remove(book)
      return {"message" : "Book Deleted Succesfully"}
  return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book Not Found")
