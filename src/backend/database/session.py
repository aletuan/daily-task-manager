from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from typing import Generator

# Database URL - in production, use environment variable
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://user:password@localhost/daily_task_manager"
)

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=300,
    echo=False  # Set to True for SQL query logging
)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get database session
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 