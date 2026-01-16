from fastapi import APIRouter
from .. import database
from ..models.schemas import User

router = APIRouter()

@router.get("/")
def get_users():
    users = [doc.to_dict() for doc in database.db.collection("users").stream()]
    return {"users": users}

@router.post("/")
def add_user(user: User):
    doc_ref = database.db.collection("users").add(user.dict())
    return {"message": "User added successfully"}
