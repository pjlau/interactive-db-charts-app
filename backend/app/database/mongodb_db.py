from pymongo import MongoClient

def get_mongo_data():
    client = MongoClient("mongodb://mongo:27017/")
    db = client["charts"]
    collection = db["hotspot"]
    data = list(collection.find({}, {"_id": 0}))
    return data