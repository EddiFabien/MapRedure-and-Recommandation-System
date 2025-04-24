import pandas as pd

def map_product_context(file_path):
    """
    Map stage: Produces a list of (context, product) pairs.
    """
    data = pd.read_csv(file_path)
    mapped = []

    for _, row in data.iterrows():
        context = (row["City"], row["Customer type"], row["Gender"])
        product = row["Product line"]
        mapped.append((context, product))

    return mapped
