import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from mapreduce.mapper import map_product_context
from mapreduce.shuffler import shuffle_mapped_data
from mapreduce.reducer import reduce_product_popularity

if __name__ == "__main__":
    # Path to the preprocessed data
    data_processed_path = "../../data/processed/data_processed.csv"

    # Perform the mapping step
    mapped_data = map_product_context(data_processed_path)
    #print("Mapped Data:", mapped_data)  # Debugging

    # Perform the shuffling step
    grouped_data = shuffle_mapped_data(mapped_data)
    print("Type of Grouped Data:", type(grouped_data))
    #print("Grouped Data:", grouped_data)

    # Ensure grouped_data is a dictionary
    if not isinstance(grouped_data, dict):
        raise TypeError("Grouped data is not a dictionary. Check the shuffle_mapped_data function.")

    # Perform the reducing step
    recommendations = reduce_product_popularity(grouped_data)
    #print("Recommendations:", recommendations)
