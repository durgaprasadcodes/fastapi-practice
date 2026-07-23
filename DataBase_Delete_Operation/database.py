from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql

DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/userdb"

engine = create_engine(DATABASE_URL)

sesionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)

def get_db():
    db = sesionLocal()
    try:
        yield db
    finally:
        db.close()
        
Base = declarative_base()
