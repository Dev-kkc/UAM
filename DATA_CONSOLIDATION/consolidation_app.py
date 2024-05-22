import pandas as pd
import os
import streamlit as st
from utils_consolidation import *



# Streamlit UI
st.title("Excel File Merger")
st.write("Upload multiple Excel files to merge them into a single file with an additional 'Application' column indicating the file name.")

uploaded_files = st.file_uploader("Choose Excel files", type="xlsx", accept_multiple_files=True)

if uploaded_files:
    output_excel = 'combined_output.xlsx'
    merge_files_to_excel(uploaded_files, output_excel)
    
    st.success(f"Files have been merged into {output_excel}.")
    
    # # Provide a download link
    # with open(output_excel, 'rb') as f:
    #     st.download_button('Download Merged Excel File', f, file_name=output_excel)
        
# Streamlit UI
st.title("Excel File Merger and Joiner")
st.write("Upload multiple Excel files to merge them into a single file with an additional 'Application' column indicating the file name.")

uploaded_files = st.file_uploader("Choose Excel files to merge", type="xlsx", accept_multiple_files=True)

if uploaded_files:
    combined_df = merge_files_to_excel(uploaded_files)
    
    st.success("Files have been merged.")
    st.dataframe(combined_df.head())  # Display the merged dataframe
    
    st.write("Upload another Excel file to perform a left join based on 'User ID'.")
    join_file = st.file_uploader("Choose Excel file for left join", type="xlsx")
    
    if join_file:
        join_df = pd.read_excel(join_file)
        st.success("Join file uploaded successfully.")
        st.dataframe(join_df.head())  # Display the join dataframe

        # Perform left join
        result_df = combined_df.merge(join_df, on='User ID', how='left')
        st.write("Resultant table after left join:")
        st.dataframe(result_df.head())  # Display the resultant dataframe
        
        output_excel = 'result_output.xlsx'
        result_df.to_excel(output_excel, index=False)
        
        # Provide a download link
        with open(output_excel, 'rb') as f:
            st.download_button('Download Resultant Excel File', f, file_name=output_excel)

