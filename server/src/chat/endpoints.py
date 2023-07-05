from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, Depends
from server.src.chat.schemas import RoomSchemas, MessageSchemas
from server.schemas import ResponseModel, ErrorResponseModel
from server.src.chat.socket import ConnectionManager
from server.src.chat.models import Room
from server.src.chat.services import (
    get_list_rooms,
    get_room_by_id,
    delete_room_by_id
)
from server.src.user.services import retrieve_user_by_id
from server.src.user.security import validate_token, IsAdmin

from datetime import datetime
from fastapi import WebSocket, WebSocketDisconnect
import json


router = APIRouter()

manager = ConnectionManager()


@router.post("/room", dependencies=[Depends(IsAdmin)])
async def create_room(room: Room = Body(...)):
    room.save()

    return ResponseModel(room, message="Ok")


@router.get("/rooms")
async def get_rooms():
    data = []
    try:
        rooms = await get_list_rooms()
        if rooms:
            for room in rooms:
                r = await get_room_by_id(room)
                host = await retrieve_user_by_id("649a83ae7a45c76a02d63954")
                print("host", host)
                data.append({
                    "pk": r.pk,
                    "name": r.name,
                    "host_id": r.host_id
                })

    except:
        ErrorResponseModel(400, "Bad")

    return ResponseModel(data, message="Ok")


@router.delete("/room/{room_id}", dependencies=[Depends(IsAdmin)])
async def delete_room(room_id: str):
    try:
        await delete_room_by_id(room_id)
        
    except:
        ErrorResponseModel(400, "Bad")

    return ResponseModel("", message="Ok")

# @router.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket, client_id: int):
#     await manager.connect(websocket)
#     now = datetime.now()
#     current_time = now.strftime("%H:%M")
#     try:
#         while True:
#             data = await websocket.receive_text()
#             # await manager.send_personal_message(f"You wrote: {data}", websocket)
#             message = {"time":current_time,"clientId":client_id,"message":data}
#             await manager.broadcast(json.dumps(message))
            
#     except WebSocketDisconnect:
#         manager.disconnect(websocket)
#         message = {"time":current_time,"clientId":client_id,"message":"Offline"}
#         await manager.broadcast(json.dumps(message))