import streamlit as st
import pandas as pd
import sys
import os

# --- Page configuration ---
st.set_page_config(page_title="Recommandation based on context", layout="wide")

# Path to the MapReduce scripts
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mapreduce')))
from mapper import map_product_context
from shuffler import shuffle_mapped_data
from reducer import reduce_product_popularity

# --- Loading and processing data ---
@st.cache_data
def load_and_process_data(path):
    mapped_data = map_product_context(path)
    shuffled_data = shuffle_mapped_data(mapped_data)
    recommendations = reduce_product_popularity(shuffled_data)
    return recommendations

# Make the absolute path to the CSV file
data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'processed', 'data_processed.csv'))

# Load recommendations
recommendations = load_and_process_data(data_path)

# --- Sidebar: Parameters & Button ---
st.sidebar.title("Customer Profile")

city = st.sidebar.selectbox("City", ["Yangon", "Mandalay", "Naypyitaw"])
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
customer_type = st.sidebar.selectbox("Customer type", ["Member", "Normal"])

# --- Button ---
calculate = st.sidebar.button("🔍 Show Recommandation")

# --- Main Page Content ---
st.markdown(
    "<h2 style='text-align: center; color: white;'>Recommended Product Lines</h2>",
    unsafe_allow_html=True,
)

# Centered content
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Optional image display
    image_path = ""  # Replace with image path if needed
    if image_path:
        st.image(image_path, use_container_width=True)

    # Only show recommendation after button is clicked
    if calculate:
        context_key = (city, customer_type, gender)
        if context_key in recommendations:
            recommended_products = recommendations[context_key]
            st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
            for i, (product, count) in enumerate(recommended_products, 1):
                st.markdown(f"<h4>{i}. {product} (x{count})</h4>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.warning("No recommendations found for this context.")
