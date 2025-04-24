import pandas as pd
import os
import load_data

print(load_data.data_frame().columns)

def preprocess_data():
    data = load_data.data_frame()
    data_processed = data[['City', 'Gender', 'Customer type', 'Product line']]
    
    # Check if the directory exists
    output_dir = os.path.join(os.path.dirname(__file__), "../../data/processed")
    os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist


    # Export to the data/processed folder
    output_path = os.path.join(output_dir, "data_processed.csv")
    data_processed.to_csv(output_path, index=False, encoding="utf-8")
    print(f"✅ Data processed successfully and saved to {output_path}")
    return data_processed

preprocess_data()