from fastapi import FastAPI
import uvicorn
from server.src.user.endpoints import router as UserRouter


app = FastAPI()
app.include_router(UserRouter, tags=["User"], prefix="/user")

@app.get("/")
def index():
    return {"message": "Welcome To User App World"}