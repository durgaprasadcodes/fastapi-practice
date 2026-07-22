from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine(F"mysql+pymysql://root:password@localhost:3306/mydb")

sessionLocal = sessionmaker(engine,autoflush=False,autocommit=False)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
    
