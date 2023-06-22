from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    username: str = Field(...)
    password: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "username": "daitech20",
                "password": "dai123"
            }
        }


class UserLoginSchema(BaseModel):
    username: str = Field(...)
    password: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "username": "daitech20",
                "password": "dai123"
            }
        }


class PutUserSchema(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "password": "dai123"
            }
        }


class PatchUserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "password": "dai123"
            }
        }