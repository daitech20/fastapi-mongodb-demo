from passlib.context import CryptContext
from server.schemas import ResponseModel, ErrorResponseModel
from server.src.user.models import Users
from bson.objectid import ObjectId
from bson.errors import InvalidId
 


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def user_helper(user) -> dict:
    return {
        "id": str(user["id"]),
        "fullname": user["fullname"],
        "email": user["email"],
        "username": user["username"],
        "password": user["password"]
    }


async def retrieve_user_by_id(user_id: str) -> dict:
    user = await Users.find_one({"_id": ObjectId(user_id)})

    if user:
        user_data = user_helper(user)
        user_data.pop("password")

        return user_data
    else:
        return False


async def retrieve_user_by_username(username: str) -> dict:
    user = await Users.find_one({"username": username})

    if user:
        return user_helper(user)
    else:
        return False


async def add_user(user_data: dict) -> dict:
    user_data["password"] = pwd_context.hash(user_data["password"])
    user = await retrieve_user_by_username(user_data["username"])
    check_user_email = await retrieve_user_by_email(user_data["email"])

    if user or check_user_email:
        return False
    else:
        user = Users(
            fullname=user_data["fullname"],
            username=user_data["username"],
            password=user_data["password"],
            email=user_data["email"]
        )
        await user.commit()

        new_user = await Users.find_one({"_id": user.id})

        return user_helper(new_user)


async def retrieve_user_by_email(email: str):
    user = await Users.find_one({"email": email})

    if user:
        return user_helper(user)
    else:
        return False


async def update_user(id: str, data: dict):
    try:
        user = await Users.find_one({"_id": ObjectId(id)})
        if user:
            check_user_email = await retrieve_user_by_email(data["email"])

            if check_user_email:
                if user_helper(user) != check_user_email:

                    raise ErrorResponseModel(400, "Email has exists!!")

            data["password"] = pwd_context.hash(data["password"])

            user.update(data)
            await user.commit()
            user_data = user_helper(user)
            user_data.pop("password")

            return ResponseModel(user_data, "User updated successfully.")
        
        else:
            raise ErrorResponseModel(400, "User not exists!!")

    except InvalidId:
        raise ErrorResponseModel(400, "User not exists!!")


async def patch_user(id: str, data: dict):
    try:
        user = await Users.find_one({"_id": ObjectId(id)})
        if user:

            if data.get("email"):
                check_user_email = await retrieve_user_by_email(data["email"])

                if check_user_email:
                    if user_helper(user) != check_user_email:

                        raise ErrorResponseModel(400, "Email has exists!!")
            else:
                data["email"] = user.email

            if data.get("password"):
                data["password"] = pwd_context.hash(data["password"])
            else:
                data["password"] = user.password
            
            if not data.get("fullname"):
                data["fullname"] = user.fullname


            user.update(data)
            await user.commit()
            user_data = user_helper(user)
            user_data.pop("password")

            return ResponseModel(user_data, "User updated successfully.")
        
        else:
            raise ErrorResponseModel(400, "User not exists!!")

    except InvalidId:
        raise ErrorResponseModel(400, "User not exists!!")


async def delete_user(id: str):
    user = await Users.find_one({"_id": ObjectId(id)})
    if user:
        # await Users.delete_one({"_id": ObjectId(id)})
        await user.delete()
        return True
    else:
        return False


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


async def authenticate_user(username: str, password: str):
    user = await retrieve_user_by_username(username)

    if not user or not verify_password(password, user["password"]):
        return False
    
    return user