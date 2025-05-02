# Projet : Prévision de la production solaire

## Introduction

### Contexte

Les centrales photovoltaïques sont de plus en plus utilisées pour produire de l'énergie renouvelable. Cependant, la production d'énergie solaire est variable et dépend de nombreux facteurs, notamment la météo. Dans ce projet, nous allons utiliser des données historiques de production d'énergie solaire et de conditions météorologiques pour prédire la production d'énergie solaire à court terme.

- DC_POWER (Direct Current) représente la puissance instantanée fournie par les panneaux photovoltaïques, en courant continu, tel que généré directement par les cellules solaires 
- AC_POWER (Alternating Current) est la puissance instantanée restituée par l’onduleur après conversion du courant continu en courant alternatif, utilisable par le réseau et les consommateurs 

Les panneaux produisent du DC ; les onduleurs (ou convertisseurs) transforment ce DC en AC, souvent avec quelques pour cents de perte (typiquement 2 %–5 %, voire jusqu’à ~25 % en cas de surdimensionnement)

## Objectif

L'objectif est de créer un modèle de machine learning capable de prédire la production d'énergie solaire à partir des données météorologiques et de production passées.

La variable cible à prédire est ``ac_power`` (la puissance active en kW).

**``dc_power`` NE PEUT PAS être utilisé comme variable explicative, car il s'agit d'une variable dérivée de ``ac_power``.**

## Jeu de données

Le jeu de données est constitué de deux fichiers CSV :
- plant_generation_data_groupe_<1, 2, 3>.csv : contient les données de production d'énergie solaire pour une centrale photovoltaïque. La granuralité temporelle est de 15 minutes.
  - ``date_time`` : date et heure de la mesure
  - ``plant_id`` : identifiant de la centrale photovoltaïque
  - ``dc_power`` : puissance continue (en kW)
  - ``ac_power`` : puissance alternative (en kW)

- Plant_Weather_Sensor_Data.csv : contient les données météorologiques pour la même centrale. La granuralité temporelle est de 15 minutes.
  - ``date_time`` : date et heure de la mesure
  - ``plant_id`` : identifiant de la centrale photovoltaïque
  - ``ambient_temperature`` : température ambiante (en °C)
  - ``module_temperature`` : température des panneaux photovoltaïques (en °C)
  - ``irradiation`` : irradiation solaire (en W/m²)

NB : Les données sont à la maille 15 minutes. La production solaire est en générale, fortement corrélée avec l'irradiation solaire. La température ambiante et la température des panneaux photovoltaïques peuvent également influencer la production d'énergie solaire.

Il n'est pas possible d'utiliser ``dc_power`` comme variable explicative, car il s'agit d'une variable dérivée de ``ac_power``. En effet, la puissance alternative est obtenue à partir de la puissance continue par un onduleur, et il n'est pas possible d'utiliser une variable dérivée pour prédire la variable d'origine.

## Organisation

Le projet Python est à réaliser en **groupe de 3**. Il y aura donc:
- 2 groupes de 3 étudiants
- 1 groupe de 4 étudiants

Le projet Python est à rendre **au plus tard le 31 juillet 2025**.

### Notation

Le projet Python sera noté sur 20 points. La note se basera sur les critères suivants:
- Qualité du code (propreté, lisibilité, modularité)
- Qualité de la documentation (commentaires, docstrings)
- Qualité de l'analyse (clarté, pertinence des visualisations, interprétation des résultats)
- Qualité de la présentation (clarté, structure)

### Le rendu

Le rendu attendu est double:
- Un rapport écrit présentant la démarche et les principaux resultats (4 pages maximum)
- Un notebook Jupyter contenant le code et les visualisations

Le rendu via un dépôt GitHub sera préféré. Vous pouvez également rendre le code via mail. Dans ce cas, il faudra s'assurer que le notebook est exécutable sans erreur.

## Détail du projet

1. **Exploration des données** : Analyser les données pour comprendre leur structure, leur contenu et leur qualité.
   1. Quels sont les types de variables disponibles ?
   2. Quelles sont les plages temporelles couvertes ?
   3. Visualiser l'évolution temporelle de la production d'énergie solaire et des données météorologiques

2. **Préparation des données (feature engineering)** : Nettoyer et préparer les données pour l'entraînement du modèle.
   1. Y'a-t-il des valeurs manquantes ?
   2. Fusionner les jeux de données météo et production
   3. Créer des variables calendaires supplémentaires
      1. Jour de la semaine
      2. Jour
      3. Heure
      4. is_day : 1 si c'est le jour, 0 sinon
   4. Créer une variable de lag
      1. ``ac_power_lag_1`` : production de la veille (attention les données sont à la maille 15 min), on utilisera ``df["ac_power"].shift(24 * 4)``.

> 
> Si vous n'arrivez pas à créer les variables demandées, ne restez pas bloqués, passez à la suite et revenez-y plus tard.
>
> Si vous pensez à d'autres variables intéressantes à créer, n'hésitez pas à les ajouter.
> 

3. **Importance des features et étude de la corrélation entre les variables**
   1. Utiliser un modèle ``RandomForestRegressor`` pour évaluer l'importance des variables : 
      1. Séparer les données en entraînement et test (train/test split avec 80% des données pour l'entraînement et 20% pour le test)
      2. Entraîner le modèle sur les données d'entraînement
      3. Évaluer l'importance des variables avec ``model.feature_importances_``
      4. Visualiser l'importance des variables avec un graphique
   2. Visualiser la matrice de corrélation entre les variables

NB:
>
> La corrélation ≠ importance de la feature, car :
> - La corrélation est linéaire et univariée
> - La feature importance dans un modèle comme RandomForest est multivariée, non linéaire, et basée sur la capacité d’une variable à réduire l’erreur de prédiction.
>

   3. Conserver uniquement les 5 variables les plus importantes pour l'entraînement du modèle (celles avec la plus grande importance)

4. **Modélisation** : Créer un modèle de machine learning pour prédire la production d'énergie solaire.
   1. Séparer les données en train/test (80% des données pour l'entraînement et 20% pour le test)
   2. Entraîner le modèle de régression linéaire (``LinearRegression``) sur les données d'entraînement
   3. Évaluer le modèle sur les données de test
   4. Afficher les métriques de performance (ex: RMSE, MAE, R²)
   5. Entrainer un modèle de régression par forêt aléatoire (``RandomForestRegressor``) sur les données d'entraînement
   6. Évaluer le modèle sur les données de test
   7. Afficher les métriques de performance (ex: RMSE, MAE, R²)
   8. Comparer les performances des deux modèles

5. **Visualisation des résultats**
   1. Visualiser les prévisions du modèle sur les données de test
   2. Comparer les prévisions avec les valeurs réelles
   3. Visualiser les résidus du modèle (différence entre les prévisions et les valeurs réelles)
   

#### Bonus

6. Prédire la valeur de ``dc_power`` (la puissance continue) à partir de ``ac_power`` (la puissance alternative) et des autres variables. 
   1. Créer un modèle de machine learning pour prédire ``dc_power`` à partir des autres variables
   2. Évaluer le modèle sur les données de test
   3. Afficher les métriques de performance (ex: RMSE, MAE, R²)
   4. Visualiser les prévisions du modèle sur les données de test
   5. Comparer les prévisions avec les valeurs réelles

7. En déduire et visualiser l'efficacité de l'onduleur sur les données prédites (ratio entre la puissance alternative et la puissance continue) : 
   1. Créer une nouvelle variable ``efficacite_onduleur`` = ``ac_power / dc_power``
   2. Visualiser l'évolution de cette variable dans le temps
   3. Analyser les variations de cette variable en fonction des conditions météorologiques

