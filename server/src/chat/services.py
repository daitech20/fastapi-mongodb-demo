from server.src.chat.models import Room
from redis_om.model import NotFoundError



async def get_list_rooms():
    rooms = Room.all_pks()
    
    return rooms


async def get_room_by_id(pk: str):
    room = Room.get(pk=pk)
    
    return room


async def delete_room_by_id(pk: str):
    room = Room.get(pk=pk)
    if room:
        room.delete(pk)
    else:
        return False
    
    return True