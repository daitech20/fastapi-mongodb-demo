from fastapi import WebSocket
import json


class ConnectionManager:

    def __init__(self):
        self.active_connections: list[WebSocket] = []
        self.client_ids: list[str] = []

    async def connect(self, websocket: WebSocket, client_id: str):
        print("connect!")
        await websocket.accept()
        self.active_connections.append(websocket)
        self.client_ids.append(client_id)
        await self.broadcast(message=f"Client id {client_id} has join the chat", client_ids=self.client_ids)

    async def disconnect(self, websocket: WebSocket, client_id: str):
        print("disconnect")
        self.active_connections.remove(websocket)
        self.client_ids.remove(client_id)

        await self.broadcast(f"Client id {client_id} has left the chat", client_ids=self.client_ids)

    async def send_personal_message(self, message: str, websocket: WebSocket, client_ids: list[str]):

        await websocket.send_json({"message": message, "client_ids": client_ids})

    async def broadcast(self, message: str, client_ids: list[str]):
        for connection in self.active_connections:
            await connection.send_json({"message": message, "client_ids": client_ids})