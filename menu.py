from fastapi import APIRouter
from .. import database
from ..models.schemas import MenuItem

router = APIRouter()

@router.get("/")
def get_menu():
    menu_items = [doc.to_dict() for doc in database.db.collection("menu").stream()]
    return {"menu": menu_items}

@router.post("/")
def add_menu_item(item: MenuItem):
    database.db.collection("menu").add(item.dict())
    return {"message": "Menu item added successfully"}
