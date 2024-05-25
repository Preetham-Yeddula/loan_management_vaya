from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
import os

from .DataStoreInterface import IDataStore

class MongoDataStore(IDataStore):
    def __init__(self, db_name: str, collection_name: str):
        mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
        self.client = AsyncIOMotorClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    async def add(self, document):
        await self.collection.insert_one(document)

    async def get(self, key):
        document = await self.collection.find_one({"_id": key})
        return document

    async def update(self, key, document):
        await self.collection.update_one({"_id": key}, {"$set": document})