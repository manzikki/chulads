import datetime   # This will be needed later
import os

from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://marko:ChulaDS2566@cluster0.q5fe942.mongodb.net/?retryWrites=true&w=majority"

# Connect to your MongoDB cluster:
client = MongoClient(MONGODB_URI)

# List all the databases in the cluster:
for db_info in client.list_database_names():
   print(db_info)

