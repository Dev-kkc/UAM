import pandas as pd
import os
import streamlit as st


def append_files_to_excel(files):
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

def split_dataframe(df, chunk_size):
    """Split a DataFrame into chunks of a specified size."""
    chunks = [df[i:i + chunk_size] for i in range(0, df.shape[0], chunk_size)]
    return chunks