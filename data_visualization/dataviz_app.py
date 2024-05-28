import streamlit as st 
import matplotlib.pyplot as plt
import pandas as pd

def data_visualization_app():
    # Check if cleaned DataFrame is in session state
    if "cleaned_df" in st.session_state:
        cleaned_df = st.session_state["cleaned_df"]
        
        # Create a Streamlit app
        st.title('Data Visualization')
        st.write("Cleaned DataFrame:")
        st.write(cleaned_df)
        
        # Visualize data using a bar chart with Matplotlib
        st.write("Bar Chart of Status Column:")
        status_counts = cleaned_df['Status'].value_counts()

        # Create the bar chart
        fig, ax = plt.subplots()
        status_counts.plot(kind='bar', ax=ax)
        ax.set_title('Status Counts')
        ax.set_xlabel('Status')
        ax.set_ylabel('Count')
        
        # Display the bar chart in Streamlit
        st.pyplot(fig)