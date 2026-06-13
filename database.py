from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# This creates a local database file named 'academia.db' automatically
DATABASE_URL = "sqlite:///./academia.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Helper tool to open and close connections safely
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()