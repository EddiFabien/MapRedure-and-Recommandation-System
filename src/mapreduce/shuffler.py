# shuffler.py
from collections import defaultdict

def shuffle_mapped_data(mapped_data):
    """
    Shuffle stage: Groups products by context.
    """
    grouped_data = defaultdict(list)

    for context, product in mapped_data:
        grouped_data[context].append(product)

    return grouped_data
