from passlib.context import CryptContext
from server.database import get_database
from bson.objectid import ObjectId
from server.schemas import ResponseModel, ErrorResponseModel
from bson.errors import InvalidId

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
db = get_database()
user_collection = db.get_collection("users")


def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "fullname": user["fullname"],
        "email": user["email"],
        "username": user["username"],
        "password": user["password"]
    }


async def retrieve_user_by_id(user_id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(user_id)})

    if user:
        return user_helper(user)
    else:
        return False


async def retrieve_user_by_username(username: str) -> dict:
    user = await user_collection.find_one({"username": username})

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
        user = await user_collection.insert_one(user_data)
        new_user = await user_collection.find_one({"_id": user.inserted_id})

        return user_helper(new_user)


async def retrieve_user_by_email(email: str):
    user = await user_collection.find_one({"email": email})

    if user:
        return user_helper(user)
    else:
        return False


async def update_user(id: str, data: dict):
    try:
        user = await user_collection.find_one({"_id": ObjectId(id)})

        if user:
            check_user_email = await retrieve_user_by_email(data["email"])

            if check_user_email:
                if user_helper(user) != check_user_email:

                    raise ErrorResponseModel(400, "Email has exists!!")

            data["password"] = pwd_context.hash(data["password"])
            updated_user = await user_collection.update_one(
                {"_id": ObjectId(id)}, {"$set": data}
            )
            if updated_user:
                user = await user_collection.find_one({"_id": ObjectId(id)})
                return ResponseModel(user_helper(user), "User updated successfully.")
            else:
                raise ErrorResponseModel(400, "Error!")
    except InvalidId:
        raise ErrorResponseModel(400, "User not exists!!")


async def delete_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
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