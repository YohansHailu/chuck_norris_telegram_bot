from pymongo import MongoClient
import os
from dotenv import load_dotenv
from Persistence.Respository import Repository

class Dbcontext:

    def __init__(self):
        load_dotenv()
        MONGODB_URL = os.getenv("MONGODB_URL")
        DB_NAME = os.getenv("DB_NAME")

        self.client = MongoClient(MONGODB_URL )
        self.db = self.client.get_database(DB_NAME)
    
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Dbcontext, cls).__new__(cls)
        return cls._instance



    def get_collection(self, collection_name):
        return self.db.get_collection(collection_name)

dbContext = Dbcontext()

user_collection_name = "users"
chuck_norris_jokes_collection_name = "chuck_norris_jokes"
tell_here_collection_name = "tell_here"
coding_jokes_collection_name = "coding_jokes"


user_repo = Repository(dbContext.get_collection(user_collection_name))
chuck_repo = Repository(dbContext.get_collection(chuck_norris_jokes_collection_name))
tell_here_repo = Repository(dbContext.get_collection(tell_here_collection_name))
coding_jokes_repo = Repository(dbContext.get_collection(coding_jokes_collection_name))
