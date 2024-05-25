from pymongo import MongoClient
import os

from .DataStoreInterface import IDataStore

class MongoDataStore(IDataStore):
    def __init__(self, db_name: str, collection_name: str):
        mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def add(self, document):
        self.collection.insert_one(document)

    def get(self, key):
        document = self.collection.find_one({"_id": key})
        return document

    def update(self, key, document):
        self.collection.update_one({"_id": key}, {"$set": document})