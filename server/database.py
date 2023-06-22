from server.settings import settings
import motor.motor_asyncio

def get_database():
    client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_URI)
    print("---Connect to mongodb----")
    
    return client[f'{settings.DATABASE_NAME}']


if __name__ == "__main__":   

    # Get the database
    db = get_database()