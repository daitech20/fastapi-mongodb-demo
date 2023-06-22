from fastapi import HTTPException


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(code, message):
    raise HTTPException(
        status_code=code, detail=message
    )