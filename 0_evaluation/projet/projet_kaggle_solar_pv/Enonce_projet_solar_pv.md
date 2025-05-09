# Projet : Prévision de la production solaire

## Introduction

### Contexte

Les centrales photovoltaïques sont de plus en plus utilisées pour produire de l'électricité. La production d'énergie solaire est variable et dépend de nombreux facteurs, notamment la météo. La prédiction de la production d'énergie solaire est un enjeu majeur pour les producteurs d'énergie et pour le gestionnaire du réseau, respectivement pour optimiser la production et pour garantir l'équilibre entre l'offre et la demande d'électricité (dispatching).

Dans ce projet, nous allons utiliser des données météorologiques pour prédire la production d'énergie solaire à court terme.

La production solaire est mesurée en kW (kilowatts) et est généralement exprimée en deux types de puissance :
- DC_POWER (Direct Current) représente la puissance instantanée fournie par les panneaux photovoltaïques, en courant continu, tel que généré directement par les cellules solaires 
- AC_POWER (Alternating Current) est la puissance instantanée restituée par l’onduleur après conversion du courant continu en courant alternatif, utilisable par le réseau et les consommateurs 

Les panneaux produisent du DC ; les onduleurs (ou convertisseurs) transforment ce DC en AC, souvent avec quelques pour cents de perte (typiquement 2 %–5 %, voire jusqu’à ~25 % en cas de surdimensionnement)

## Objectif

L'objectif est de créer un modèle de machine learning capable de prédire la variable ``dc_power`` (la puissance en courant continu) à partir des autres variables disponibles dans le jeu de données.

**``ac_power`` NE PEUT PAS être utilisé comme variable explicative, car il s'agit d'une variable dérivée de ``dc_power``.**

## Jeu de données

Vous disposez de 4 csv:
- **plant_generation_data_groupe_<1, 2, 3>.csv** : contient les données de production d'énergie solaire pour une centrale photovoltaïque. La granularité temporelle est de 15 minutes.
- **plant_weather_data_groupe_<1, 2, 3>.csv** : contient les données météorologiques pour la même centrale. La granularité temporelle est de 15 minutes.
- **plant_weather_forecast_groupe_<1, 2, 3>.csv**: contient les prévisions météorologiques pour la même centrale. La granularité temporelle est de 15 minutes.
- **target_groupe_<1, 2, 3>.csv**: contient la plage horaire à prédire.

#### Détail:
- **plant_generation_data_groupe_<1, 2, 3>.csv** : contient les données de production d'énergie solaire pour une centrale photovoltaïque. La granularité temporelle est de 15 minutes.
  - ``date_time`` : date et heure de la mesure
  - ``plant_id`` : identifiant de la centrale photovoltaïque
  - ``dc_power`` : puissance en courant continu (en kW)
  - ``ac_power`` : puissance en courant alternatif (en kW)

- **plant_weather_data_groupe_<1, 2, 3>.csv** : contient les données météorologiques pour la même centrale. La granularité temporelle est de 15 minutes.
  - ``date_time`` : date et heure de la mesure
  - ``plant_id`` : identifiant de la centrale photovoltaïque
  - ``ambient_temperature`` : température ambiante (en °C)
  - ``module_temperature`` : température des panneaux photovoltaïques (en °C)
  - ``irradiation`` : irradiation solaire (en W/m²)
  
- **plant_weather_forecast_groupe_<1, 2, 3>.csv**: contient les prévisions météorologiques pour la même centrale. La granularité temporelle est de 15 minutes.
  - ``date_time`` : date et heure de la mesure
  - ``plant_id`` : identifiant de la centrale photovoltaïque
  - ``ambient_temperature`` : température ambiante (en °C)
  - ``module_temperature`` : température des panneaux photovoltaïques (en °C)
  - ``irradiation`` : irradiation solaire (en W/m²)
  
- **target_groupe_<1, 2, 3>.csv**: contient la plage horaire à prédire.
  - ``date_time`` : date et heure de la mesure
  - ``plant_id`` : identifiant de la centrale photovoltaïque

NB : Les données sont à la maille 15 minutes. La production solaire est en général fortement corrélée avec l'irradiation solaire. La température ambiante et la température des panneaux photovoltaïques peuvent également influencer la production d'énergie solaire.

Il n'est pas possible d'utiliser ``ac_power`` comme variable explicative, car il s'agit d'une variable dérivée de ``dc_power``. En effet, la puissance en courant alternatif est obtenue à partir de la puissance en courant continu par un onduleur, et il n'est pas possible d'utiliser une variable dérivée pour prédire la variable d'origine. Ainsi, dans le jeu de données target_groupe_<1, 2, 3>.csv, on observe que la variable ``ac_power`` est absente.

## Organisation

Le projet Python est à réaliser **en groupe**. Il y aura donc:
- 2 groupes de 3 étudiants
- 1 groupe de 4 étudiants

Le projet Python est à rendre **au plus tard le 31 juillet 2025**.

### Notation

Le projet Python sera noté sur 20 points. La note se basera sur les critères suivants:
- Qualité du code (propreté, lisibilité, modularité)
- Qualité de la documentation (commentaires, docstrings)
- Qualité de l'analyse (clarté, pertinence des visualisations, interprétation des résultats, performance du modèle)
- Qualité de la présentation (clarté, structure)

### Le rendu

Le rendu attendu est:
- Un rapport écrit présentant la démarche et les principaux résultats (4 pages maximum avec les figures)
- Un notebook Jupyter contenant le code et les visualisations OU une application streamlit exécutable

Le rendu via un dépôt GitHub sera préféré. Vous pouvez également rendre le code via mail. Dans ce cas, il faudra s'assurer que le notebook ou l'application streamlit est exécutable sans erreur.

## Détail du projet

1. **Exploration des données**: lire les données ``plant_generation_data_groupe_<1, 2, 3>.csv`` et ``plant_weather_data_groupe_<1, 2, 3>.csv``
   1. Quels sont les types de variables disponibles ?
   2. Quelles sont les plages temporelles couvertes ?
   3. Visualiser l'évolution temporelle de la production d'énergie solaire et des données météorologiques

2. **Préparation des données (feature engineering)**
   1. Y'a-t-il des valeurs manquantes ?
   2. Fusionner les jeux de données météo et production
   3. Créer des variables calendaires à partir de la variable ``date_time`` :
      1. Jour de la semaine
      2. Jour
      3. Heure
      4. is_day : 1 si c'est le jour, 0 sinon
         1. (jour: entre 6h et 18h, nuit: entre 18h et 6h)
   4. Packager la création de variable dans une fonction ``create_features(df)`` qui prend en entrée un DataFrame et renvoie un DataFrame avec les nouvelles variables créées.

> 
> Si vous n'arrivez pas à créer les variables demandées, ne restez pas bloqués, passez à la suite et revenez-y plus tard.
>
> Si vous pensez à d'autres variables intéressantes à créer, n'hésitez pas à les ajouter et à les justifier.
> 

3. **Importance des features et étude de la corrélation entre les variables**
   1. Utiliser un modèle ``RandomForestRegressor`` pour évaluer l'importance des variables : 
      1. Séparer les données en X (variables explicatives) et y (variable cible)

      ```python
      X = df.drop(
         ["date_time", "plant_id", "dc_power", "ac_power"],
         axis=1,
      )
      y = df["dc_power"]
      ```

      2. Entraîner le modèle sur les données
      3. Évaluer l'importance des variables avec ``model.feature_importances_``
      4. Visualiser l'importance des variables avec un graphique

      NB:
      >
      > La corrélation ≠ importance de la feature, car :
      > - La corrélation est linéaire et univariée
      > - La feature importance dans un modèle comme RandomForest est multivariée, non linéaire, et basée sur la capacité d’une variable à réduire l’erreur de prédiction.
      >

   3. Conserver uniquement les 5 variables les plus importantes pour l'entraînement du modèle (celles avec la plus grande importance). Quelle est la variable la plus importante ?

   4. Y'a-t-il des variables corrélées entre elles dans les données sélectionnées ? 
      1. Visualiser la matrice de corrélation entre les variables (on utilisera ``df.corr()`` et une heatmap)
      2. Identifier les variables corrélées entre elles (corrélation > 0.9)
      3. Supprimer une des deux variables corrélées (la moins importante) de l'analyse
   5. Créer une fonction ``create_final_dataset(df)`` qui prend en entrée un DataFrame et renvoie un DataFrame avec les variables sélectionnées pour l'entraînement du modèle.


4. **Modélisation** : Créer un modèle de machine learning pour prédire la production d'énergie solaire.
   1. Séparer les données en train/test (80% des données pour l'entraînement et 20% pour le test)
   2. Entraîner le modèle de régression linéaire (``LinearRegression``) sur les données d'entraînement
   3. Évaluer le modèle sur les données de test
   4. Afficher les métriques de performance (ex: RMSE, MAE, R²)
   5. Entraîner un modèle de régression par forêt aléatoire (``RandomForestRegressor``) sur les données d'entraînement
   6. Évaluer le modèle sur les données de test
   7. Afficher les métriques de performance (ex: RMSE, MAE, R²)
   8. Comparer les performances des deux modèles

5. **Visualisation des résultats**
   1. Lire les données de test: ``target_groupe_<1, 2, 3>.csv`` et ``plant_weather_forecast_groupe_<1, 2, 3>.csv``
   2. Fusionner les données de test avec les prévisions météo
   3. Appliquer les transformations nécessaires

   ```python
   df_to_pred = pd.read_csv(f'target_groupe_<1, 2, 3>.csv')
   df_to_pred["date_time"] = pd.to_datetime(df_to_pred["date_time"])

   weather_forecast = pd.read_csv(f'plant_weather_forecast_groupe_<1, 2, 3>.csv')
   weather_forecast["date_time"] = pd.to_datetime(weather_forecast["date_time"])
   
   df_to_pred = df_to_pred.merge(
      weather_forecast,
      how="inner",
      on=["date_time", "plant_id"],
   )

   df_to_pred_features = create_features(df=df_to_pred)
   df_to_pred_selected = create_final_dataset(
      df=df_to_pred_features,
      feature_selected=feature_selected,
   )
   df_to_pred_selected.head()
   ```

   4. Appliquer le meilleur modèle (celui ayant la métrique R² la plus élevée) sur les données de test
   5. Visualiser les prévisions du modèle
   

### Bonus

6. Prédire la valeur de ``ac_power`` (la puissance en courant alternatif) à partir **des prédictions** de ``dc_power`` (la puissance en courant continu) et des autres variables. 
   1. Créer un modèle de machine learning pour prédire ``ac_power`` à partir des autres variables et des prédictions de ``dc_power``.
   2. Évaluer le modèle sur les données de test
   3. Afficher les métriques de performance (ex: RMSE, MAE, R²)
   4. Visualiser les prévisions du modèle sur les données de test
   5. Comparer les prévisions avec les valeurs réelles

7. Ajouter la prévision de ``ac_power`` dans le DataFrame ``df_to_pred_selected`` et visualisez l'évolution de la puissance en courant alternatif dans le temps.
 
8. En déduire et visualiser l'efficacité de l'onduleur sur les données prédites (ratio entre la puissance en courant alternatif et la puissance en courant continu) : 
   1. Créer une nouvelle variable ``efficacite_onduleur`` = ``ac_power / dc_power``
   2. Visualiser l'évolution de cette variable dans le temps ainsi que celles de ``dc_power`` et ``ac_power``
   3. Analyser les variations de cette variable en fonction des conditions météorologiques

9. **Résidus**:
   1. Reprenez le modèle de régression linéaire de la question 4.2 et calculez les résidus (erreurs de prédiction) sur les données de test
   2. Visualiser les résidus en fonction des valeurs prédites