# Function to connect db
from ..config.settings import settings
from pymongo import MongoClient


# Create a MongoDB client
client = MongoClient(settings.mongo_url)


# Access the desired database (replace 'your_database_name' with your actual database name)
db = client['chatapp']

def get_db():
    return db  # You can return the database instance directly


# Example usage: getting a collection
# print(db.list_collection_names())  # This will print the list of collections in the database