from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT
from database.mongodb import db


async def connect_to_mongo():
    db.client = AsyncIOMotorClient(str(MONGODB_URL), maxPoolSize=MAX_CONNECTIONS_COUNT, minPoolSize=MIN_CONNECTIONS_COUNT)


async def close_mongo_connection():
    db.client.close()
