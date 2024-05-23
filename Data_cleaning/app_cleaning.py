import pandas as pd
import streamlit as st
from Data_cleaning.cleaning_utils import *

def data_cleaning_app():
    # Extract unique categories from the 'status' column
    if "result_df" in st.session_state:
        result_df = st.session_state["result_df"]

    unique_categories = result_df['Status'].unique()

    # Create a Streamlit app
    st.title('Categorize Status Column')
    st.write("Original DataFrame:")
    st.write(result_df)
    # Instructions
    st.write("Select and map the categories to respective boxes:")

    # Create three columns for the new categories
    active_categories = st.multiselect('Active', options=unique_categories, default=[])
    inactive_categories = st.multiselect('Inactive', options=unique_categories, default=[])
    pending_categories = st.multiselect('Pending', options=unique_categories, default=[])

    # Button to apply the mapping
    if st.button('Apply Mapping'):
        # Apply the mapping to the DataFrame
        df = apply_mapping(result_df, active_categories, inactive_categories, pending_categories)

        # Show updated DataFrame
        st.write("Updated DataFrame:")
        st.write(df)

