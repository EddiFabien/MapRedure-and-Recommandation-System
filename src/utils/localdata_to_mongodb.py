import pandas as pd
from pymongo import MongoClient

def import_data_to_mongodb(csv_path, mongo_uri, database_name, collection_name):
    """
    Import data from a CSV file into a MongoDB collection.

    Args:
        csv_path (str): Path to the CSV file.
        mongo_uri (str): MongoDB connection URI.
        database_name (str): Name of the database.
        collection_name (str): Name of the collection.

    Returns:
        None
    """
    # Read CSV data into a DataFrame
    df = pd.read_csv(csv_path)

    # Convert DataFrame to a list of dictionaries (Mongo-friendly format)
    data = df.to_dict(orient="records")

    # Connect to MongoDB
    client = MongoClient(mongo_uri)

    # Use database and collection
    db = client[database_name]
    collection = db[collection_name]

    # Insert data
    collection.insert_many(data)

    print(f"✅ Data from {csv_path} imported successfully into {database_name}.{collection_name}.")