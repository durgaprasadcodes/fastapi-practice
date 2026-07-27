from sqlalchemy import Column ,VARCHAR ,Integer
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,autoincrement=True,primary_key=True)
    name = Column(VARCHAR(255),nullable=False)
    email = Column(VARCHAR(255),nullable=False,unique=True)
    password = Column(VARCHAR(20),nullable=False)
    