from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_USER = "root"
DATABASE_PASSWORD = "password"
DATABASE_HOST = "localhost"
DATABASE_PORT = "3306"
MYSQL_DATABASE = "mydb" 


engine = create_engine(F"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{MYSQL_DATABASE}")

sessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
    finally:
        db.close()
        
Base = declarative_base()