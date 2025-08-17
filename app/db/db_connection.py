#database.db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # go up from /app to /In5
DB_PATH = BASE_DIR / "database.db"
SQLALCHEMY_DATABASE = f"sqlite:///{DB_PATH}"

engine=create_engine(SQLALCHEMY_DATABASE,connect_args={"check_same_thread":False})

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()