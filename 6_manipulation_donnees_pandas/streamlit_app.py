import streamlit as st
import pandas as pd
import os

# Set the page configuration
st.set_page_config(
    page_title="MIMO - Chapitre 4 - Les fonctions",
    page_icon=":python:",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("MIMO - Chapitre 6 - Pandas")

path = os.path.join(os.getcwd(), "6_manipulation_donnees_pandas", "data", "communes-france-2025.csv")

df = pd.read_csv(path)
st.dataframe(df)