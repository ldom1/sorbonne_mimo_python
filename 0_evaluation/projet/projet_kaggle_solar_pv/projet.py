import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np


# Fonction pour charger les données
def load_data(file_path):
    return pd.read_csv(file_path)


# Fonction pour prétraiter les données
def preprocess_data(generation_data, weather_data):
    generation_data = generation_data.rename(
        columns={
            "DATE_TIME": "date_time",
            "PLANT_ID": "plant_id",
            "SOURCE_KEY": "source_key",
            "DC_POWER": "dc_power",
            "AC_POWER": "ac_power",
            "DAILY_YIELD": "daily_yield",
            "TOTAL_YIELD": "total_yield",
        }
    )
    generation_data["date_time"] = pd.to_datetime(generation_data["date_time"])
    generation_data_gr = generation_data.groupby(
        by=["date_time", "plant_id"],
        as_index=False,
    ).agg(
        {
            "dc_power": "sum",
            "ac_power": "sum",
        }
    )

    weather_data = weather_data.rename(
        columns={
            "DATE_TIME": "date_time",
            "PLANT_ID": "plant_id",
            "SOURCE_KEY": "source_key",
            "AMBIENT_TEMPERATURE": "ambient_temperature",
            "MODULE_TEMPERATURE": "module_temperature",
            "IRRADIATION": "irradiation",
        }
    )
    weather_data["date_time"] = pd.to_datetime(weather_data["date_time"])
    weather_data_gr = weather_data.groupby(
        by=["date_time", "plant_id"],
        as_index=False,
    ).agg(
        {
            "ambient_temperature": "mean",
            "module_temperature": "mean",
            "irradiation": "mean",
        }
    )

    df = generation_data_gr.merge(
        weather_data_gr,
        how="inner",
        on=["date_time", "plant_id"],
    )
    df = df.dropna(how="any")
    return df


# Fonction pour créer des caractéristiques
def create_features(df):
    df["date_time"] = pd.to_datetime(df["date_time"])
    df["day"] = df["date_time"].dt.day
    df["hour"] = df["date_time"].dt.hour
    df["day_of_week"] = df["date_time"].dt.dayofweek
    df["is_day"] = (df["date_time"].dt.hour >= 6) & (df["date_time"].dt.hour < 18)
    return df


# Fonction pour sélectionner les caractéristiques importantes
def select_important_features(df, target_pred):
    X = df.drop(
        ["date_time", "plant_id", "dc_power", "ac_power"],
        axis=1,
    )
    y = df[target_pred]

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    importances = model.feature_importances_
    feature_names = X.columns
    indices = np.argsort(importances)[::-1]
    feature_selected = [feature_names[i] for i in indices if importances[i] > 10**-4]

    return feature_selected, X[feature_selected], y


# Fonction pour entraîner le modèle
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, shuffle=False
    )
    model = RandomForestRegressor(
        n_estimators=100, random_state=42, min_samples_leaf=10, max_features=0.5
    )
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    r2_score = model.score(X_test, y_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred)

    return model, y_test, y_pred, r2_score, mae, rmse


# Interface Streamlit
st.title("Prévision de la production d'énergie solaire")

# Chargement des fichiers
group = 1

# add selectbox to choose the group
group = st.selectbox("Sélectionner le groupe", [1, 2, 3])

if group:
    base_path = "0_evaluation/projet/projet_kaggle_solar_pv"

    generation_data = load_data(
        file_path=f"{base_path}/data/plant_generation_data_groupe_{group}.csv"
    )
    weather_data = load_data(
        file_path=f"{base_path}/data/plant_weather_data_groupe_{group}.csv"
    )
    weather_forecast_data = load_data(
        file_path=f"{base_path}/data/plant_weather_forecast_groupe_{group}.csv"
    )
    target_data = load_data(file_path=f"{base_path}/data/target_groupe_{group}.csv")

    df = preprocess_data(generation_data, weather_data)
    df = create_features(df)

    target_pred = st.selectbox(
        "Sélectionner la cible à prédire", ["dc_power", "ac_power"]
    )

    feature_selected, X, y = select_important_features(df, target_pred)
    model, y_test, y_pred, r2_score, mae, rmse = train_model(X, y)

    st.write(f"R² score: {r2_score:.2f}")
    st.write(f"MAE: {mae:.2f}")
    st.write(f"RMSE: {rmse:.2f}")

    # Affichage des graphiques
    st.subheader("Prédictions vs Valeurs réelles")
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=np.arange(len(y_test)),
            y=y_test,
            mode="lines",
            name="Valeurs réelles",
            line=dict(color="blue"),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=np.arange(len(y_test)),
            y=y_pred,
            mode="lines",
            name="Prédictions",
            line=dict(color="red"),
        )
    )
    fig.update_layout(
        title="Prédictions vs Valeurs réelles",
        xaxis_title="Index",
        yaxis_title="Valeurs",
        legend_title="Légende",
    )
    st.plotly_chart(fig)

    st.subheader("Importance des caractéristiques")
    importances = model.feature_importances_
    feature_names = X.columns
    indices = np.argsort(importances)[::-1]
    plt.figure(figsize=(10, 6))
    plt.title("Importance des caractéristiques")
    plt.bar(range(X.shape[1]), importances[indices], align="center")
    plt.xticks(range(X.shape[1]), feature_names[indices], rotation=90)
    plt.xlim([-1, X.shape[1]])
    st.pyplot(plt)

    st.subheader("Corrélation des caractéristiques")
    correlation_matrix = X.corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", square=True)
    st.pyplot(plt)
