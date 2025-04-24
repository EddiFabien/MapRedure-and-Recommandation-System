from collections import defaultdict, Counter

def reduce_product_popularity(grouped_data):
    """
    Reduce stage: Aggregates product frequency and returns top 3 products by context.
    """
    popular_products = {}

    for context, products in grouped_data.items():
        counts = Counter(products)
        popular_products[context] = counts.most_common(3)

    return popular_products
