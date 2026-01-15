from fastapi import APIRouter
from ..database import db
from ..models.schemas import Memory

router = APIRouter()

@router.get("/")
def get_memories():
    memories = [doc.to_dict() for doc in db.collection("memories").stream()]
    return {"memories": memories}

@router.post("/")
def add_memory(memory: Memory):
    db.collection("memories").add(memory.dict())
    return {"message": "Memory added successfully"}
