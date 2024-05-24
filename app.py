import streamlit as st
from Data_cleaning.app_cleaning import * 
from DATA_CONSOLIDATION.consolidation_app import * 

# Custom CSS to change the sidebar style
st.markdown(
    """
    <style>
    /* Change the background color of the sidebar */
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
    /* Change the font color of the sidebar text */
    .sidebar .sidebar-content .css-17eq0hr {
        color: #333333;
    }
    /* Change the style of the sidebar title */
    .sidebar .sidebar-content .css-1cpxqw2 {
        font-size: 24px;
        color: #000000;
    }
    /* Change the style of the radio buttons */
    .sidebar .sidebar-content .css-1d391kg {
        font-size: 18px;
        color: #444444;
    }
    /* Add padding to the sidebar */
    .sidebar .sidebar-content {
        padding: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit UI
st.title("Multipage Excel Tool")
st.sidebar.title("Navigation")

# Navigation options (modify based on your app names)
page_names = ["Data Upload", "Categorize Status"]
page_functions = [data_consolidation_app, data_cleaning_app]

selected_page = st.sidebar.radio("Select a page", page_names)

# Display the selected app
for idx, page_name in enumerate(page_names):
    if selected_page == page_name:
        page_functions[idx]()
        break
