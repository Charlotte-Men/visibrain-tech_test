from motor.motor_asyncio import AsyncIOMotorClient
from backend.config import MONGO_URI, MONGO_DB_NAME

client = AsyncIOMotorClient(MONGO_URI)
database = client[MONGO_DB_NAME]
games_collection = database["games"]
