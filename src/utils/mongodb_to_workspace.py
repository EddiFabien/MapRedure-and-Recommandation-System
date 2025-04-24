from pymongo import MongoClient
import pandas as pd

def fetch_data_from_mongodb(uri, database_name, collection_name):
    """
    Fetch data from a MongoDB collection and return it as a Pandas DataFrame.

    Args:
        uri (str): MongoDB connection URI.
        database_name (str): Name of the database.
        collection_name (str): Name of the collection.

    Returns:
        pd.DataFrame: Data from the collection as a DataFrame.
    """
    # Connect to MongoDB
    mongo_client = MongoClient(uri)
    db = mongo_client[database_name]
    collection = db[collection_name]

    # Fetch data from the collection
    cursor = collection.find({})
    data = [doc for doc in cursor]

    # Convert ObjectId to string
    for doc in data:
        doc["_id"] = str(doc["_id"])

    # Convert to DataFrame
    return pd.DataFrame(data)
