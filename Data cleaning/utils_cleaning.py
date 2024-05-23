import pandas as pd
import numpy as np

def apply_mapping(df, active_categories, inactive_categories, pending_categories):
    """
    Apply user-defined status mappings to the DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the 'status' column to be updated.
    active_categories (list): List of categories to be mapped to 'Active'.
    inactive_categories (list): List of categories to be mapped to 'Inactive'.
    pending_categories (list): List of categories to be mapped to 'Pending'.

    Returns:
    pd.DataFrame: The updated DataFrame with the 'status' column mapped.
    """
    # Create mapping dictionary
    category_mapping = {}
    for category in active_categories:
        category_mapping[category] = 'Active'
    for category in inactive_categories:
        category_mapping[category] = 'Inactive'
    for category in pending_categories:
        category_mapping[category] = 'Pending'

    # Apply mapping to DataFrame
    df['Status'] = df['Status'].map(category_mapping)

    return df


