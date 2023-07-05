from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from server.src.chat.socket import ConnectionManager
from datetime import datetime
import json


ws = FastAPI()
room_manager = ConnectionManager()


@ws.get("/users")
async def get_active_user_rooms():
    return {"users": room_manager.client_ids}


@ws.websocket("/rooms/{client_id}")
async def websocket_room(websocket: WebSocket, client_id: str):
    await room_manager.connect(websocket, client_id)
    try:
        while True:
            data = await websocket.receive_text()
            await room_manager.send_personal_message(message=f"You wrote {data}", client_ids=room_manager.client_ids, websocket=websocket)
            await room_manager.broadcast(message=f"Client ID #{client_id} says: {data}", client_ids=room_manager.client_ids)

    except:
        await room_manager.disconnect(websocket=websocket, client_id=client_id)
        # await room_manager.broadcast(f"Client ID #{client_id} left the chat", client_ids=room_manager.client_ids)