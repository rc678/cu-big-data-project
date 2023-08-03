from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# Replace with your PostgreSQL configuration
DB_URL = "postgresql://:@localhost:5432"

# Create the database engine
engine = create_engine(DB_URL)

# Base class for your models
Base = declarative_base()

# Create a session class to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# SQLAlchemy model for the User table
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String)

    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email


# Create the tables in the database
Base.metadata.create_all(bind=engine)
