import streamlit as st
import pandas as pd

import os
import plotly.express as px

# Set the page configuration
st.set_page_config(
    page_title="Devoir maison - Master MIMO - 2025",
    page_icon=":python:",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Devoir maison - Master MIMO - 2025")

# Load data
data_file_path = os.path.join(
    os.getcwd(),
    "0_evaluation",
    "devoir_maison",
    "data_analysis_with_streamlit",
    "data",
    "AIML Dataset.csv",
)
df = pd.read_csv(data_file_path)

# Display the dataframe in the app
st.write("## AIML Dataset")
st.dataframe(df)
