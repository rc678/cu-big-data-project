from http.client import HTTPException
from os import name
import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models import User, SessionLocal
from pydantic import BaseModel
from typing import List

app = FastAPI()

# TODO Change origin from all to specific urls
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to fetch all users
@app.get("/users", response_model=List[UserResponse])
def get_all_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users

# Endpoint to create a new user
@app.post("/users", response_model=UserResponse)
def create_user(username: str, email: str, db: Session = Depends(get_db)):
    # Check if the user already exists
    existing_user = db.query(User).filter(User.username == username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = User(username=username, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # Refresh the new_user object to get the updated ID after committing

    return new_user

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
