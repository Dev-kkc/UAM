import streamlit as st
import pandas as pd

# Sample DataFrame for demonstration
data = {
    'status': ['New', 'Completed', 'In Progress', 'On Hold', 'Cancelled', 'Pending Review']
}
df = pd.DataFrame(data)

# Extract unique categories from the 'status' column
unique_categories = df['status'].unique()

# Create a Streamlit app
st.title('Categorize Status Column')

# Create three columns for the new categories
category_mapping = {}
for category in unique_categories:
    st.write(f"Map status '{category}' to:")
    new_category = st.selectbox(
        label=f"Select new category for '{category}'",
        options=['Active', 'Inactive', 'Pending'],
        key=category
    )
    category_mapping[category] = new_category

# Show the mapping dictionary
st.write("Mapping Dictionary:")
st.write(category_mapping)

# # Function to apply the mapping to the DataFrame
# def map_status(df, mapping):
#     df['status'] = df['status'].map(mapping)
#     return df

# # Button to apply the mapping
# if st.button('Apply Mapping'):
#     df = map_status(df, category_mapping)
#     st.write("Updated DataFrame:")
#     st.write(df)

