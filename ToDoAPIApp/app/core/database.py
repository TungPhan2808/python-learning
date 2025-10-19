import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
dbName = os.getenv("DATABASE_NAME")

click = AsyncIOMotorClient(MONGO_URI)
db = click[dbName]
users_collection = db["users"]
todos_collection = db["todos"]