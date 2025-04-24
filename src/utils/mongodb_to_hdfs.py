from pymongo import MongoClient
from hdfs import InsecureClient
import json

# 🔹 Connecting à MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["bigdata_project"]  # Use your database name
collection = db["supermarket_sales"]  # Use your collection name

# 🔹 Connecting to HDFS
hdfs_client = InsecureClient("http://localhost:9870", user="hadoop")

# 🔹 Select the data from MongoDB
cursor = collection.find({})  # Select all collections
data = [doc for doc in cursor]  # Convert in list

# 🔹 Transforming in JSON (supprimer l'ObjectId qui n'est pas sérialisable)
for doc in data:
    doc["_id"] = str(doc["_id"])  # Convert ObjectId in string

json_data = json.dumps(data, indent=4)  # JSON format readable

# 🔹 Import data into HDFS
hdfs_path = "/user/hadoop/mongodb_data/supermarket_sales.json"  # Specify your HDFS path
with hdfs_client.write(hdfs_path, encoding='utf-8') as writer:
    writer.write(json_data)

print(f"✅ Data migrated successfully into {hdfs_path} in HDFS")

