import pandas as pd
import streamlit as st
from utils_cleaning import *

df= pd.read_csv("Consolidated.csv")

# Extract unique categories from the 'status' column
unique_categories = df['Status'].unique()

# Create a Streamlit app
st.title('Categorize Status Column')
st.write("Original DataFrame:")
st.write(df)
# Instructions
st.write("Select and map the categories to respective boxes:")

# Create three columns for the new categories
active_categories = st.multiselect('Active', options=unique_categories, default=[])
inactive_categories = st.multiselect('Inactive', options=unique_categories, default=[])
pending_categories = st.multiselect('Pending', options=unique_categories, default=[])

# Button to apply the mapping
if st.button('Apply Mapping'):
    # Apply the mapping to the DataFrame
    df = apply_mapping(df, active_categories, inactive_categories, pending_categories)

    # Show updated DataFrame
    st.write("Updated DataFrame:")
    st.write(df)

# # Print type and contents of pending_categories for verification
# st.write("Type of pending_categories:", type(pending_categories))
# st.write("Contents of pending_categories:", pending_categories)

# Display the original DataFrame
