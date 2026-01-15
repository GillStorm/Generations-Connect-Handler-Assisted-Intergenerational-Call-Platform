from fastapi import APIRouter
from ..database import db
from ..models.schemas import User

router = APIRouter()

@router.get("/")
def get_users():
    users = [doc.to_dict() for doc in db.collection("users").stream()]
    return {"users": users}

@router.post("/")
def add_user(user: User):
    doc_ref = db.collection("users").add(user.dict())
    return {"message": "User added successfully"}
