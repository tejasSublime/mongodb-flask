from pymongo.mongo_client import MongoClient
import os
from dotenv import load_dotenv


def connectiontest():
# Load the .env file
    # load_dotenv()

    # Replace the placeholder with your Atlas connection string
    # uri = "<connection string>"

    # Create a new client and connect to the server
    # client = MongoClient(os.environ.get("MONGODB_URI"))
    # client = MongoClient("mongodb+srv://test:sublimetechnocorp@cluster0.0aaafyp.mongodb.net")
    client = MongoClient(
        host="mongodb://localhost:27017/",
        port=27017,
        authSource="admin"
    )

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(e)
        print("Unable to connect to the MongoDB server.")