from fastapi import APIRouter
from server.src.user.endpoints import router as UserRouter
from server.src.chat.endpoints import router as ChatRouter


router = APIRouter()
router.include_router(UserRouter, tags=["User"], prefix="/user")
router.include_router(ChatRouter, tags=["Chat"], prefix="/chat")