from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None
    name: str
    email: str

class MenuItem(BaseModel):
    id: Optional[str] = None
    name: str
    description: str
    price: float

class Memory(BaseModel):
    id: Optional[str] = None
    title: str
    description: str

class CallRequest(BaseModel):
    student_name: str
    student_phone: str
    elder_name: str
    handler_phone: str
