from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv


load_dotenv()  # 👈 Loads variables from .env into os.environ

DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
