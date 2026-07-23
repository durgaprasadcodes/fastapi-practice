from database import Base
from sqlalchemy import Column,INTEGER,VARCHAR,VARCHAR

class Book(Base):
    __tablename__ = "books"
    id = Column(INTEGER,primary_key=True,autoincrement=True)
    title = Column(VARCHAR(255))
    author = Column(VARCHAR)
    date = Column(VARCHAR(255))
    email = Column(VARCHAR(255))