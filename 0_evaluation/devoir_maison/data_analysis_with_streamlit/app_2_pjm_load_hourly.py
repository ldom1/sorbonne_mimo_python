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
    "PJM_Load_hourly.csv",
)
df = pd.read_csv(data_file_path)
df["Datetime"] = pd.to_datetime(df["Datetime"])

# Display the dataframe in the app
st.write("## PJM Load Hourly Data")
st.dataframe(df)

## Statistics on the dataframe
st.write("## Statistiques")
st.write(f"#### Nombre de points de données: {df.shape[0]}")
st.write(f"#### Consommation moyenne: {df['PJM_Load_MW'].mean()} MW")
st.write(
    f"#### Consommation maximale: {df['PJM_Load_MW'].max()} MW à {df['Datetime'][df['PJM_Load_MW'].idxmax()]}"
)
st.write(
    f"#### Consommation minimale: {df['PJM_Load_MW'].min()} MW à {df['Datetime'][df['PJM_Load_MW'].idxmin()]}"
)
st.write(f"#### Année de début: {df['Datetime'].min()}")
st.write(f"#### Année de fin: {df['Datetime'].max()}")

## Question
st.write(
    "## Quel est le mois avec la consommation moyenne la plus élevée pour l'année sélectionnée ?"
)
years = sorted(df["Datetime"].dt.year.unique())
selected_year = st.selectbox("Sélectionner une année", years)
st.write(f"Vous avez sélectionné l'année : **{selected_year}**")

df_selected_year = df[df["Datetime"].dt.year == selected_year]
df_selected_year["Month_name"] = df_selected_year["Datetime"].dt.month_name()
df_selected_year_grouped = (
    df_selected_year.groupby("Month_name")["PJM_Load_MW"].mean().reset_index()
)
month_max = df_selected_year_grouped["PJM_Load_MW"].idxmax()
month_max_value = df_selected_year_grouped["PJM_Load_MW"].max()

st.write(
    f"Le mois avec la consommation maximale est le mois **{df_selected_year_grouped['Month_name'][month_max]}** avec une consommation de **{month_max_value} MW**."
)

## Afficher un graphique
st.write("## Graphique de la consommation pour une année sélectionnée")
st.write("Sélectionner une année pour afficher le graphique de la consommation")
selected_year_graph = st.selectbox("Sélectionner une année", years, key="graph")
df_selected_year_graph = df[df["Datetime"].dt.year == selected_year_graph]

fig = px.line(
    df_selected_year_graph,
    x="Datetime",
    y="PJM_Load_MW",
    title=f"Consommation PJM pour l'année {selected_year_graph}",
    labels={"Datetime": "Date", "PJM_Load_MW": "Consommation (MW)"},
)

fig.update_layout(xaxis_title="Date", yaxis_title="Consommation (MW)")
st.plotly_chart(fig, use_container_width=True)
