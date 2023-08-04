from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import User, SessionLocal
from pydantic import BaseModel

app = FastAPI()

# TODO Change origin from all to specific urls
origins = [
'*'
]


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

# Endpoint to fetch all users
@app.get("/users", response_model=None)
def get_all_users(limit: int = 10):
    db = SessionLocal()
    try:
        users = db.query(User).limit(limit).all()
        return users
    finally:
        db.close()

# Endpoint to create a new user
@app.post("/users", response_model=UserResponse)
def create_user(username: str, email: str):
    db = SessionLocal()
    try:
        # Check if the user already exists
        existing_user = db.query(User).filter(User.username == username).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")

        new_user = User(username=username, email=email)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)  # Refresh the new_user object to get the updated ID after committing

        return UserResponse(id=new_user.id, username=new_user.username, email=new_user.email)
    finally:
        db.close()
