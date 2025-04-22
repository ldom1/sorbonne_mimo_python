import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# Set the page configuration
st.set_page_config(
    page_title="Devoir maison - Master MIMO - 2025",
    page_icon=":python:",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Devoir maison - Master MIMO - 2025")


# Function to load and preprocess data
def load_data(file_path: str) -> pd.DataFrame:
    """Load and preprocess the data from a CSV file."""
    df = pd.read_csv(file_path)
    df["runtime_float"] = df["Runtime"].str.extract(r"(\d+)").astype(float)
    return df


# Function to get statistics
def get_statistics(df: pd.DataFrame) -> dict:
    """Calculate and return statistics from the dataframe."""
    stats = {
        "num_movies": df.shape[0],
        "num_unique_genres": len(df["Genre"].unique()),
        "avg_runtime": df["runtime_float"].mean(),
    }
    return stats


# Function to get the best movie by director
def get_best_movie_by_director(df: pd.DataFrame, director: str) -> pd.Series:
    """Get the best movie by a specific director."""
    best_movie = (
        df[df["Director"] == director]
        .sort_values(by="Meta_score", ascending=False)
        .iloc[0]
    )
    return best_movie


# Function to get average scores by year for a specific genre
def get_avg_scores_by_year(df: pd.DataFrame, genre: str) -> pd.DataFrame:
    """Get average scores by year for a specific genre."""
    filtered_df = df[df["Genre"] == genre]
    avg_scores = filtered_df.groupby("Released_Year")["Meta_score"].mean().reset_index()
    return avg_scores


# Load data
data_file_path = os.path.join(
    os.getcwd(),
    "0_evaluation",
    "devoir_maison",
    "data_analysis_with_streamlit",
    "data",
    "imdb_top_1000.csv",
)
df = load_data(data_file_path)

# Display the dataframe in the app
st.write("## IMDB Top 1000 Movies")
st.dataframe(df)

# Display statistics
st.write("## Statistiques")
stats = get_statistics(df=df)
st.metric("#### Nombre de films", stats['num_movies'])
st.metric("#### Nombre de genres uniques", stats['num_unique_genres'])
st.metric("#### Durée moyenne des films (en minutes)", stats['avg_runtime'])

# User interaction: Best movie by director
st.write("## Quel est le film le mieux noté du réalisateur sélectionné ?")
directors = sorted(df["Director"].unique())
selected_director = st.selectbox("Sélectionner un réalisateur", directors)
st.write(f"Vous avez sélectionné le réalisateur : **{selected_director}**")

st.write("Voici le film le mieux noté de ce réalisateur :")
best_movie = get_best_movie_by_director(df, selected_director)
st.write(f"**Titre :** {best_movie['Series_Title']}")
st.write(f"**Année :** {best_movie['Released_Year']}")
st.write(f"**Note :** {best_movie['Meta_score']}")

# Visualization: Average scores by year for a specific genre
st.write("## Graphique des notes des films par année")
st.write("### Sélectionner un genre")
genres = sorted(df["Genre"].unique())
selected_genre = st.selectbox("Sélectionner un genre", genres)
st.write(f"Vous avez sélectionné le genre : **{selected_genre}**")

st.write("### Evolution des notes par année")
st.write("Voici l'évolution des notes des films par année pour le genre sélectionné :")
avg_scores_by_year = get_avg_scores_by_year(df=df, genre=selected_genre)

st.line_chart(avg_scores_by_year.set_index("Released_Year")["Meta_score"])
