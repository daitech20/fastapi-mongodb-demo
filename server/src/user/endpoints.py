from server.schemas import ResponseModel, ErrorResponseModel
from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder
from datetime import timedelta, datetime
from server.src.user.schemas import (
    UserSchema,
    UserLoginSchema,
    PutUserSchema,
    PatchUserSchema
)
from server.src.user.services import (
    retrieve_user_by_id,
    add_user,
    update_user,
    delete_user,
    authenticate_user,
    patch_user
)
from server.src.user.security import validate_token
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from server.settings import settings
from zoneinfo import ZoneInfo
import bson


router = APIRouter()


class Settings(BaseModel):
    authjwt_secret_key: str = settings.SECRET_KEY


@AuthJWT.load_config
def get_config():
    return Settings()


@router.get("/{user_id}", dependencies=[Depends(validate_token)])
async def get_user_by_id(user_id: str):
    try:
        user = await retrieve_user_by_id(user_id)
    except:
        return ErrorResponseModel(400, "Not a valid ObjectId, it must be a 12-byte input or a 24-character hex string")
    
    return ResponseModel(user, "Get user successfully.")


@router.post("/register", response_description="Add user to database")
async def add_user_data(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    
    if new_user:
        return ResponseModel(new_user, "User added successfully.")
    else:
        return ErrorResponseModel(400, "Username or email was exists!")



@router.put("/update/{id_user}", response_description="User data updated in to the database", dependencies=[Depends(validate_token)])
async def update_user_data(id_user: str, user_data: PutUserSchema = Body(...)):
    user_data = jsonable_encoder(user_data)

    return await update_user(id_user, user_data)


@router.patch("/update/{id_user}", response_description="User data updated in to the database", dependencies=[Depends(validate_token)])
async def update_user_data(id_user: str, user_data: PatchUserSchema = Body(...)):
    user_data = jsonable_encoder(user_data)

    return await patch_user(id_user, user_data)


@router.delete("/update/{id_user}", response_description="User was deleted ", dependencies=[Depends(validate_token)])
async def delete_user_data(id_user: str):
    try:
        check_delete = await delete_user(id_user)
        if check_delete:
            return ResponseModel("", "User deleted successfully.")
        else:
            return ErrorResponseModel(400, "Can't find user id!")
    except bson.errors.InvalidId as e:
        return ErrorResponseModel(400, "Not a valid ObjectId, it must be a 12-byte input or a 24-character hex string")


@router.post("/login")
async def login(
    Authorize: AuthJWT = Depends(),
    user: UserLoginSchema = Body(...)
):
    user = jsonable_encoder(user)
    user = await authenticate_user(user["username"], user["password"])

    if not user:

        return ErrorResponseModel(401, "Incorrect username or password")

    access_token = Authorize.create_access_token(
        subject=user["username"],
        expires_time=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    refresh_token = Authorize.create_refresh_token(
        subject=user["username"],
        expires_time=timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    )
    user.pop("password")
    data = {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "expires_time": datetime.now(tz=ZoneInfo("Asia/Ho_Chi_Minh")) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        "user": user
    }

    return ResponseModel(data, "Login successful!")