import pandas as pd
import os
import streamlit as st

def append_files_to_excel(files, output_excel):
    # List to hold dataframes
    dataframes = []

    for file in files:
        # Read the Excel files
        df = pd.read_excel(file)

        # Add a new column 'Application' with the filename (without extension)
        filename = file.name
        df['Application'] = os.path.splitext(filename)[0]

        # Append the dataframe to the list
        dataframes.append(df)
    
    # Concatenate all dataframes
    combined_df = pd.concat(dataframes, ignore_index=True)

    # Save the combined dataframe to an Excel file
    combined_df.to_excel(output_excel, index=False)
    
    
    
def merge_files_to_excel(files):
    # List to hold dataframes
    dataframes = []

    for file in files:
        # Read the Excel file
        df = pd.read_excel(file)

        # Add a new column 'Application' with the filename (without extension)
        filename = file.name
        df['Application'] = os.path.splitext(filename)[0]

        # Append the dataframe to the list
        dataframes.append(df)
    
    # Concatenate all dataframes
    combined_df = pd.concat(dataframes, ignore_index=True)
    
    return combined_df