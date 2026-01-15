from fastapi import FastAPI
from .database import initialize_firebase
from .routes import users, menu, memories
from .routes import calls


app = FastAPI()

# Initialize Firebase
initialize_firebase()

# Include routes
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(menu.router, prefix="/menu", tags=["Menu"])
app.include_router(memories.router, prefix="/memories", tags=["Memories"])
app.include_router(calls.router)

@app.get("/")
def home():
    return {"message": "Generations Connect Backend Running ✅"}
