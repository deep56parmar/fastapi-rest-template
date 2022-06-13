from mongoengine import *
import os


def connectDB():
    try:
        print("Connecting to MongoDB...", os.environ['MONGO_URL'])
        connect(db=os.environ['MONGO_DB_NAME'], host=os.environ['MONGO_URL'])
    except Exception as e:
        print(e)
        print("Error: MongoDB connection failed")
        exit(1)
