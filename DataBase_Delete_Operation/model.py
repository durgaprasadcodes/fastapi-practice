from database import Base
from sqlalchemy import Column,INTEGER,VARCHAR

class Users(Base):
    __tablename__ = "users"
    id = Column(INTEGER,primary_key=True,autoincrement=True)
    name = Column(VARCHAR(255))
    age = Column(INTEGER)
    mobile = Column(VARCHAR(255))
    email= Column(VARCHAR(100),unique=True)
    