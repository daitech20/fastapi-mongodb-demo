from fastapi import Depends
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from server.settings import settings
from fastapi_jwt_auth.exceptions import MissingTokenError, InvalidHeaderError
from server.schemas import ErrorResponseModel
from server.src.user.services import retrieve_user_by_username


class Settings(BaseModel):
    authjwt_secret_key: str = settings.SECRET_KEY


@AuthJWT.load_config
def get_config():
    return Settings()


def validate_token(Authorize: AuthJWT = Depends()):
    """
    Decode JWT token to get username => return username
    """
    try:
        Authorize.jwt_required()
        Authorize.get_jwt_subject()

    except MissingTokenError:
        raise ErrorResponseModel(400, "Token not exists")
    except InvalidHeaderError:
        raise ErrorResponseModel(401, "Token not valid")
    except:
        raise ErrorResponseModel(401, "Signature has expired")


async def IsAdmin(Authorize: AuthJWT = Depends()):
    """
    Decode JWT token to get username => return username
    """
    try:
        Authorize.jwt_required()
        username = Authorize.get_jwt_subject()
        user = await retrieve_user_by_username(username)
        if user["is_superuser"] == False:
            return ErrorResponseModel(401, "You do not have permission.")

    except MissingTokenError:
        raise ErrorResponseModel(400, "Token not exists")
    except InvalidHeaderError:
        raise ErrorResponseModel(401, "Token not valid")
    except:
        raise ErrorResponseModel(401, "Signature has expired")