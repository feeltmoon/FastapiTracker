# backend/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./my_database.db"

engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}  # needed for SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Dependency function to get DB session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
