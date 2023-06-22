from fastapi import APIRouter
from server.src.user.endpoints import router as UserRouter

router = APIRouter()
router.include_router(UserRouter, tags=["User"], prefix="/user")