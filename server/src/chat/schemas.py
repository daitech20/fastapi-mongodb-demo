from redis_om import HashModel
from server.src.chat.config import redis_db
from typing import Optional
from datetime import datetime
from zoneinfo import ZoneInfo


class RoomSchemas(HashModel):
    name: str
    host_id: str

    class Meta:
        database: redis_db


class MessageSchemas(HashModel):
    user_id: str
    fullname: str
    room_id: str
    content: str
    created_at: Optional[datetime] = datetime.now(tz=ZoneInfo("Asia/Ho_Chi_Minh"))

    class Meta:
        database: redis_db