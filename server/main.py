from fastapi import FastAPI
from server.routers.api_v1 import router as api_v1

app = FastAPI()
app.include_router(api_v1, tags=["Api V1"], prefix="/api/v1")

@app.get("/")
def index():
    return {"message": "Welcome To FastAPI World"}