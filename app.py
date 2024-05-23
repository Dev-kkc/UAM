import streamlit as st
from Data_cleaning.app_cleaning import * 
from DATA_CONSOLIDATION.consolidation_app import * 

# Streamlit UI
st.title("Multipage Excel Tool")
st.sidebar.title("Navigation")

# Navigation options (modify based on your app names)
page_names = ["Data Upload", "Categorize Status"]
page_functions = [data_consolidation_app, data_cleaning_app]

selected_page = st.sidebar.selectbox("Select a page", page_names)

# Display the selected app
for idx, page_name in enumerate(page_names):
  if selected_page == page_name:
    page_functions[idx]()
    break
