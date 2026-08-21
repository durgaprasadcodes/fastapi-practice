from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from utils.util import DATABASE_URL

engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()