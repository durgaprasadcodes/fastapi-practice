from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = 'mysql+pymysql://root:password@localhost:3306/users'

engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(autoflush=False,autocommit = False,bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
        
Base = declarative_base()
