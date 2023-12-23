from pymongo import MongoClient


class Repository:
    def __init__(self, connectionUrl, db_name, collection_name):
        self.client = MongoClient(connectionUrl)
        self.db = self.client.get_database(db_name)
        self.collection = self.db.get_collection(collection_name)

    def get_all(self):
        return self.collection.find()

    def get_by_id(self, id):
        return self.collection.find_one({"_id": id})

    def get_by_chat_id(self, chat_id):
        return self.collection.find_one({"chat_id": chat_id})

    def get_by_name(self, name):
        return self.collection.find_one({"name": name})

    def add(self, obj):
        self.collection.insert_one(obj)

    def update(self, obj):
        self.collection.update_one({"_id": obj["_id"]}, {"$set": obj})

    def delete(self, id):
        self.collection.delete_one({"_id": id})
