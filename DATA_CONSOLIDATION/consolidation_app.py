import pandas as pd
import os
import streamlit as st
from DATA_CONSOLIDATION.utils_consolidation import *


def data_consolidation_app():
    # Streamlit UI
    st.title("Excel File Merger and Joiner")
    st.write("Upload multiple Excel files to merge them into a single file with an additional 'Application' column indicating the file name.")

    uploaded_files = st.file_uploader("Choose Excel files to merge", type="xlsx", accept_multiple_files=True)

    if uploaded_files:
        combined_df = append_files_to_excel(uploaded_files)
        
        st.success("Files have been merged.")
        st.dataframe(combined_df.head())  # Display the merged dataframe
        
        st.write("Upload another Excel file to perform a left join based on 'User Id'.")
        join_file = st.file_uploader("Choose Excel file for left join", type="xlsx")
        
        if join_file:
            join_df = pd.read_excel(join_file)
            st.success("Join file uploaded successfully.")
            st.dataframe(join_df.head())  # Display the join dataframe

            # Perform left join
            result_df = combined_df.merge(join_df, on='User Id', how='left')
            st.session_state["result_df"] = result_df
            st.write("Resultant table after left join:")
            st.dataframe(result_df.head())  # Display the resultant dataframe
            
            output_excel = 'result_output.xlsx'
            result_df.to_excel(output_excel, index=False)
            
            # Provide a download link
            with open(output_excel, 'rb') as f:
                st.download_button('Download Resultant Excel File', f, file_name=output_excel)
        



