from fastapi import FastAPI, WebSocket
from server.routers.api_v1 import router as api_v1
from fastapi.middleware.cors import CORSMiddleware
from server.src.chat.ws import ws
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_v1, tags=["Api V1"], prefix="/api/v1")
app.mount("/ws", ws)


@app.get("/")
def index():
    return {"message": "Welcome To FastAPI World"}