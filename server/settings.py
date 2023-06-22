import os
from typing import Optional
from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGODB_URI: Optional[str] = os.environ.get("MONGODB_URI")
    ACCESS_TOKEN_EXPIRE_MINUTES: Optional[int] = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")
    REFRESH_TOKEN_EXPIRE_DAYS: Optional[int] = os.environ.get("REFRESH_TOKEN_EXPIRE_DAYS")
    DATABASE_NAME: Optional[str] = os.environ.get("DATABASE_NAME")
    SECRET_KEY: Optional[str] = os.environ.get("SECRET_KEY")


settings = Settings()