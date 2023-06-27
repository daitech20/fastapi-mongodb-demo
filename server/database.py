from server.settings import settings
import motor.motor_asyncio
import asyncio
from umongo.frameworks import MotorAsyncIOInstance


def get_database():
    client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_URI)
    print("---Connect to mongodb----")
    
    return client[f'{settings.DATABASE_NAME}']


def get_umongo_instance():
    motor_client = get_database()
    motor_client.get_io_loop = asyncio.get_running_loop
    instance = MotorAsyncIOInstance(motor_client)

    return instance


if __name__ == "__main__":   

    # Get the database
    db = get_database()
    instance = get_umongo_instance()