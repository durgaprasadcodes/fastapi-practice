from database import Base
from sqlalchemy import Column,Integer,String

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(150),nullable=False)
    email = Column(String(150),nullable=False)
    password = Column(String(150),nullable=False)
