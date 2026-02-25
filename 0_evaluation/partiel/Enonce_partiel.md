# Partiel - Programmation en langage Python - J5P22615

**Durée: 2 heures 30**

Le partiel est composé de trois parties :
1. QCM (7.5 points)
2. Questions ouvertes (6 points)
3. Analyse de données avec Pandas (6.5 points)

Les parties 1 et 2 seront à rendre sur papier ainsi que les réponses des questions de la partie 3. La partie 3 sera à réaliser dans un notebook Jupyter. Vous devez envoyer le notebook complété par e-mail, avec pour objet : **'Partiel - Programmation en langage Python - J5P22615 - [Votre Nom]'** à l'adresse suivante : `louis@giron-dom.eu` et en cc `Louis.Giron@univ-paris1.fr`. Le notebook doit être envoyé à la fin de l'épreuve. Aucun retard ne sera accepté.

## Partie 1 - QCM (7.5 points)

Chaque question du QCM vous rapportera 0.25 point, pour un total de 7.5 points. Répondez aux questions en cochant la bonne réponse, il peut y avoir une ou plusieurs réponses correctes.

Si vous faites une erreur, vous ne perdrez pas de point.

**1. Quel est le type de données de la variable x dans l'instruction x = 5 ?**

- [x] int
- [ ] float
- [ ] str
- [ ] bool

**2. Quelle est la valeur de y après l'exécution des instructions suivantes : x = 5; y = x > 3 ?**

- [ ] 5
- [x] True
- [ ] False
- [ ] None

**3. Comment accède-t-on au premier élément d'une liste `liste` ?**

- [x] liste[0]
- [ ] liste[1]
- [ ] liste[-1]
- [ ] liste.get(0)

**4. Quelle est la méthode pour ajouter un élément à la fin d'une liste ?**

- [ ] liste.append(element)
- [ ] liste.add(element)
- [ ] liste.insert(element)
- [ ] liste.push(element)

**5. Quelle est la syntaxe correcte pour écrire une boucle while qui s’exécute tant que x est inférieur à 10 ?**

- [ ] while x < 10:
- [ ] while (x < 10):
- [ ] while x <= 10:
- [ ] while x < 10

**6. Quel est le résultat de ``for i in range(5): print(i)`` ?**
- [ ] 0 1 2 3 4
- [ ] 1 2 3 4 5
- [ ] 0 1 2 3 4 5
- [ ] 1 2 3 4

**7. Quel est l'effet du mot-clé `continue` dans une boucle for en Python ?**

- [ ] Il passe immédiatement à l’itération suivante de la boucle
- [ ] Il arrête complètement la boucle
- [ ] Il sort de la boucle et exécute le code après la boucle
- [ ] Il relance la boucle depuis le début

**8. Comment gérer les exceptions en Python ?**
- [ ] Avec des blocs try-except
- [ ] Avec des blocs if-else
- [ ] Avec des blocs while
- [ ] Avec des blocs match-case

**9. Qu'est-ce qu'un array NumPy ?**
- [ ] Une structure de données unidimensionnelle pour stocker des nombres
- [ ] Une structure de données multidimensionnelle pour stocker des nombres
- [ ] Une structure de données pour stocker des chaînes de caractères
- [ ] Une structure de données pour stocker des listes

**10. Quel est l'avantage principal d'utiliser NumPy par rapport aux listes Python ?**
- [ ] NumPy est plus rapide pour les opérations mathématiques et permet le calcul vectorisé
- [ ] Les listes Python ne gèrent pas les nombres à virgule flottante alors que NumPy le fait
- [ ] NumPy est plus facile à utiliser que les listes Python
- [ ] Il n'y a pas d'avantage, NumPy est juste une autre façon de stocker des données

**11. Qu'est-ce qu'un DataFrame dans Pandas ?**

- [ ] Une structure de données multidimensionnel basé sur NumPy
- [ ] Une structure de données unidimensionnelle basée sur NumPy
- [ ] Une structure de données stockant des données non structurées basé sur NumPy
- [ ] Un package Python pour la manipulation de données

**12. Quelle instruction permet de fusionner deux DataFrames `df1` et `df2` sur la colonne 'ID' pour créer un DataFrame d3 ayant les colonnes ID, Name et Age ?**

**df1 :**

|   |   ID | Name    |
|---|------|---------|
| 0 |    1 | Alice   |
| 1 |    2 | Bob     |
| 2 |    3 | Charlie |

**df2 :**

|   |   ID |   Age |
|---|------|-------|
| 0 |    1 |    30 |
| 1 |    2 |    25 |
| 2 |    4 |    40 |


- [ ] ``pd.merge(df1, df2, on='ID')``
- [ ] ``pd.concat([df1, df2], axis=1)``
- [ ] ``pd.merge(df1, df2, on='id')``
- [ ] ``df1.append(df2, ignore_index=True)``

**13. À quoi sert la fonction plt.show() dans Matplotlib ?**

- [ ] À sauvegarder un graphique
- [ ] À afficher un graphique à l'écran
- [ ] À créer un nouveau graphique
- [ ] À supprimer un graphique

**14. Quel type de graphique est le plus adapté pour visualiser des catégories ?**
- [ ] Un histogramme
- [ ] Un graphique en barres
- [ ] Un graphique en ligne
- [ ] Un nuage de points

**15. Quel type de graphique est le plus adapté pour visualiser la relation entre deux variables continues ?**
- [ ] Un nuage de points
- [ ] Un histogramme
- [ ] Un graphique en barres
- [ ] Un graphique en ligne

**16. Quel est le rôle d’un masque NumPy ?**

- [ ] Filtrer ou sélectionner une partie des données d’un tableau sur la base d’une condition
- [ ] Modifier de façon permanente les types de tous les éléments
- [ ] N’ajoute qu’un seul élément à la fois
- [ ] Permet d’accélérer le chargement d’un fichier CSV

**17. Quel exemple exprime correctement l’utilisation d’un masque pour obtenir les valeurs strictement supérieures à 10 dans un tableau `a` ?**

- [ ] a[a > 10]
- [ ] a[> 10]
- [ ] mask(a, 10)
- [ ] a.select(10)

**18. Comment obtenir la somme de toutes les valeurs d’une colonne 'Valeur' d’un DataFrame Pandas nommé `df` ?**

- [ ] df['Valeur'].sum()
- [ ] df['Valeur'].mean()
- [ ] df.sum('Valeur')
- [ ] df.agg('sum')

**19. Laquelle de ces opérations est une agrégation dans Pandas ?**

- [ ] df.groupby('colonne').mean()
- [ ] df.plot()
- [ ] df.query()
- [ ] df.sort_values()

**20. Comment indiquer le type des paramètres et du retour d'une fonction en Python ?**

- [ ] En utilisant les annotations de type (ex: def f(x: int) -> float)
- [ ] En déclarant les types dans un fichier séparé
- [ ] En utilisant la fonction type()
- [ ] Ce n'est pas possible en Python

**21. Quelle différence existe-t-il entre un paramètre positionnel et un paramètre nommé dans la définition d'une fonction Python ?**

- [ ] Un paramètre positionnel doit être passé dans l'ordre, un paramètre nommé peut être précisé par son nom lors de l'appel
- [ ] Les deux doivent toujours être passés dans l'ordre
- [ ] Les paramètres nommés ne peuvent pas avoir de valeur par défaut
- [ ] Il n'y a aucune différence

**22. Quel modèle mathématique permet de représenter le lien linéaire entre deux variables ?**

- [ ] La régression linéaire
- [ ] Le clustering
- [ ] L'analyse en composantes principales
- [ ] L’arbre de décision

**23. En apprentissage automatique, à quoi correspond la classification ?**

- [ ] À prédire à quelle catégorie appartient une observation (valeur discrète)
- [ ] À prévoir une valeur numérique continue à partir de variables indépendantes
- [ ] À calculer la moyenne d’une variable
- [ ] À transformer un texte en nombre

**24. Qu'est-ce que l'apprentissage non supervisé ?**
- [ ] Un type d'apprentissage où les données ne sont pas étiquetées et l'algorithme doit trouver des structures dans les données
- [ ] Un type d'apprentissage où les données sont étiquetées et l'algorithme apprend à prédire ces étiquettes
- [ ] Un type d'apprentissage où l'algorithme est entraîné à partir de données étiquetées et non étiquetées
- [ ] Un type d'apprentissage où l'algorithme est entraîné à partir de données étiquetées uniquement

**25. Quels sont les grands principes de l'entraînement d'un modèle de machine learning ?**
- [ ] Séparer les données en ensembles d'entraînement et de test, choisir un modèle, entraîner le modèle sur l'ensemble d'entraînement, évaluer le modèle sur l'ensemble de test
- [ ] Charger les données, choisir un modèle, entraîner le modèle sur l'ensemble des données, évaluer le modèle sur l'ensemble des données
- [ ] Séparer les données en ensembles d'entraînement et de test, choisir un modèle, entraîner le modèle sur l'ensemble de test, évaluer le modèle sur l'ensemble des données
- [ ] Séparer les données en ensembles d'entraînement et de test, choisir un modèle, entraîner le modèle sur l'ensemble d'entraînement, évaluer le modèle sur l'ensemble des données

**26. Dans Scikit-learn, quelle est la fonction utilisée pour diviser les données en ensembles d'entraînement et de test ?**
- [ ] train_test_split()
- [ ] split_data()
- [ ] data_split()
- [ ] divide_data()

**27. Dans Scikit-learn, à quoi correspondant l'attribut ``n_estimators`` dans un modèle d'ensemble comme Random Forest ?**
- [ ] Au nombre d'arbres dans la forêt
- [ ] Au nombre de variables à considérer pour chaque arbre
- [ ] Au nombre de feuilles dans chaque arbre
- [ ] Au nombre de données à utiliser pour entraîner chaque arbre

**28. Avec quelles métriques peut-on évaluer la performance d'un modèle de régression ?**
- [ ] Mean Absolute Error (MAE), Mean Squared Error (MSE), R-squared
- [ ] Accuracy, Precision, Recall
- [ ] F1 Score, ROC AUC, Log Loss
- [ ] Confusion Matrix, Cross-Validation Score, Feature Importance

**29. Qu'est-ce que le sur-apprentissage (overfitting) en machine learning ?**
- [ ] Un modèle qui s'adapte trop bien aux données d'entraînement et ne généralise pas bien sur de nouvelles données
- [ ] Un modèle qui ne s'adapte pas assez aux données d'entraînement et a une performance faible
- [ ] Un modèle qui est trop simple et ne capture pas la complexité des données
- [ ] Un modèle qui est trop complexe et qui ne permet pas de faire de bonnes prédictions

**30. Parmi les types de données suivants, lesquels Pandas peut-il lire et manipuler directement ?**

- [ ] Données structurées (ex : tables de bases de données relationnelles)
- [ ] Données semi-structurées (ex : fichiers CSV, JSON, XML)
- [ ] Données non-structurées (ex : images, fichiers audio, vidéos)
- [ ] Toutes les réponses ci-dessus

## Partie 2 - Questions ouvertes (6 points)

Chaque question vaut **1.5 points**. Pensez à bien numéroter vos réponses.

1. Décrivez le principe de responsabilité unique. Quels sont les avantages de ce principe en termes de maintenance et de lisibilité du code ? Donnez un exemple concret illustrant ce principe.

2. Décrivez le concept de calcul vectorisé avec NumPy et son impact sur les performances par rapport aux boucles traditionnelles. Illustrez avec un exemple.

3. Expliquez le lien entre NumPy et Pandas. Illustrez cette relation par un exemple concret où l'on utilise les capacités de NumPy pour effectuer un filtrage de données dans un DataFrame Pandas.

4. Quelles sont les étapes typiques de prétraitement des données avant de les utiliser dans un modèle de machine learning ? Décrivez chaque étape et donnez un exemple concret pour chacune.

## Partie 3 - Analyse de données avec Pandas (6.5 points + 1.5 points bonus)

Pour cette partie, vous allez travailler sur un fichier CSV contenant les données d'une étude. Vous devez répondre aux questions en utilisant les packages Python vus en classe. 

Récupérez le fichier ``data_partiels.csv``.
- Depuis Google Drive: [Lien Google Drive](https://drive.google.com/file/d/1rTb6WnRCaH7DqpUoTR-9JYMpxMgnGG-N/view?usp=sharing)

Si vous avez un compte Kaggle, vous pouvez également télécharger le jeu de données depuis Kaggle:
- [Lien Kaggle](https://www.kaggle.com/datasets/adilshamim8/social-media-addiction-vs-relationships)
- Download
- Download dataset as zip

#### Questions

1. Charger le fichier: ``data_partiels.csv`` dans un DataFrame Pandas. Que contient ce dataframe ? Quelle est la taille de ce DataFrame ? (le nombre de lignes et de colonnes) _(0.5 points)_
2. Créer un nouveau dataframe à partir DU DataFrame chargé à la question 1, en ne gardant que les colonnes suivantes, en les renommant: _(0.5 point)_
   - `Student_ID` -> `etudiant_id`
   - `Age` -> `age`
   - `Gender` -> `genre`
   - `Avg_Daily_Usage_Hours` -> `utilisation_horaire_moyenne_jour`
   - `Most_Used_Platform` -> `plateforme_principale`
   - `Sleep_Hours_Per_Night` -> `heures_de_sommeil_par_nuit`
   - `Addicted_Score` -> `score_addiction`
   - `Mental_Health_Score` -> `score_sante_mentale`

   - `Most_Used_Platform` -> `plateforme_principale`
3. Créez une fonction prenant en entrée une Series Pandas et renvoyant la moyenne de cette série ainsi que le maximum et le minimum. Si la Series contient des valeurs nulles, affichez "La série <Nom de la série> contient des valeurs nulles", et les remplacer par la moyenne de la valeur de la série. Appliquez cette fonction à la colonne `utilisation_horaire_moyenne_jour` et `age` du DataFrame créé à la question 2. Quel est l'âge moyen ? _(1.5 point)_
4. Pour les étudiants dont la plateforme principale est Tiktok, quelle est l'utilisation moyenne horaire journalière  ? Comment varie-t-il selon le genre ? _(1 points)_
5. Quel est le pourcentage d'étudiants dont la plateforme principale est Instagram et qui ont un temps de sommeil inférieur à 7 heures par nuit ? _(1 point)_
6. Créez un graphique montrant la moyenne du score d'addiction par plateforme principale. _(1 point)_
7. Créez un graphique montrant la relation entre le score d'addiction et le score de santé mentale. Commentez ce graphique. _(1 point)_

**Bonus: _(1.5 point)_**
1. Quel est le score R² du modèle de régression linéaire entre le score d'addiction et le score de santé mentale ? _(1 point)_
2.  Que peut-on conclure de ce score R² ? _(0.5 point)_