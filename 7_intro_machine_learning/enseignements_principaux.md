# Chapitre 7 - Introduction au Machine Learning (notes pour slide)

## 7.1 - Introduction
- Le Machine Learning consiste a entrainer un modele a partir de donnees pour faire des predictions (ou des decisions) sur de nouvelles donnees.

## 7.2 - Types d'apprentissage
- Apprentissage supervise:
  - classification: predire une classe (ex: Iris)
  - regression: predire une valeur numerique
- Apprentissage non supervise (idee): decouvrir des structures dans les donnees (ex: regroupements).

## Classification: decision tree (Iris)
- Dataset typique: `Iris` (classes, features).
- Un arbre de decision apprend une regle de partage (features) pour predire la classe.

## Regression (projet Python)
- Cas pratique: remplacement des valeurs manquantes.
- Strategie simple vue:
  - remplacer par la moyenne de la colonne (puis comparer ameliorations).

## Feature Engineering
- Construire / transformer des variables (features) pour mieux decrire le probleme.
- Importance des variables:
  - identifier les features les plus liees a la cible pour guider l'amelioration du modele.

## Modelisation / Prediction
- Entrainement puis prediction sur de nouvelles donnees.
- Ameliorer le score en iterant (preprocessing, feature engineering, choix du modele).

## Comparer les modeles
- Comparer des scores (meilleur score => modele plus adapte sur le scenario etudie).

## Potentiel ajout (avec le lien correspondant)
- `train/test split` et evaluation generale (empeche de juger le modele sur les donnees vues) ([OpenClassrooms](https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python))
- Cross-validation et notions overfitting/underfitting (valider la generalisation) ([CFORPRO](https://www.cforpro.com/formation-python.php?gad_source=1&gad_campaignid=13436643100&gclid=Cj0KCQjw4PPNBhD8ARIsAMo-icxJIrVzrE8UA09lM649JzmYGU5SapWhgejE0kAKAvp27w5KUt7bz2QaApfgEALw_wcB))
- Normalisation/standardisation et pipelines `sklearn` (preprocessing coherent entre entrainement/prediction) ([Cours Python PDF](https://python.sdv.u-paris.fr/cours-python.pdf))
- Metrics (accuracy pour classification, RMSE pour regression) ([OpenClassrooms](https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python))

