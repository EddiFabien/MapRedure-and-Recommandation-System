import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import pandas as pd
from utils.mongodb_to_workspace import fetch_data_from_mongodb

def data_frame():
    return fetch_data_from_mongodb(
        uri="mongodb://localhost:27017/",
        database_name="bigdata_project",
        collection_name="supermarket_sales"
    )
