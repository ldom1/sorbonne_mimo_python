# Chapitre 6 - Manipulation de donnees avec Pandas (notes pour slide)

## Rappels
- Import: `import pandas as pd`
- Une `DataFrame` = table (lignes/colonnes) et un `Series` = une seule colonne (ou une seule dimension).

## 1. Creer un DataFrame
- Depuis un dictionnaire: `pd.DataFrame({...})`
- Depuis un CSV: `pd.read_csv(...)`
- Depuis un JSON: `pd.read_json(...)`
- Idee: aligner les colonnes/labels pour des operations propres.

## 2. Selection et filtrage
- Par nom de colonne:
  - une colonne: `df["col"]`
  - plusieurs colonnes: `df[["c1", "c2"]]`
- Par condition (filtrage bool):
  - `df[df["age"] > 30]`

## 3. Manipulation et operations
- Ajouter une colonne: `df["new"] = ...`
- Modifier une colonne: `df["col"] = ...`
- Supprimer une colonne: `del df["col"]` ou `df.drop(...)`
- Renommer: `df.rename(columns={"old": "new"})`
- Trier: `df.sort_values("col")`

## 4. Agregation de donnees: `groupby`
- Principe: grouper puis agreger
- Exemple: `df.groupby("ville")["age"].mean()`
- Agregations multiples: moyenne + somme, etc.

## 5. Visualisation
- Graphique simple (ex): barre pour une Serie/une colonne agregee
  - souvent via `matplotlib` (ou `df.plot(...)` si utilise)

## 6. Manipulation d'index
- `loc` (labels) vs `iloc` (positions)
- `at` / `iat` pour acces unitaire rapide (par label/position)

## 7. Fusion de DataFrames
- `merge` (equivalent SQL, par cles)
- `concat` (concatener sur axes, avec alignements)

## 8. Fonctions et fonctions avancees
- `apply` (souvent sur une colonne ou sur les lignes)
- Fonction anonyme (lambda) dans `apply`
- `map` pour appliquer une fonction element par element (souvent sur une Serie)

## Potentiel ajout (avec le lien correspondant)
- Installation/gestion des bibliotheques (principe `pip`) et import de modules pour integrer `pandas`/scientific stack ([OpenClassrooms](https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python))
- Lecture de fichiers Excel / exploration:
  - `pd.read_excel`, `df.describe()` ([OpenClassrooms](https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python))
- Gestion des donnees manquantes et conversions:
  - `df.dropna()`, `df.fillna()`, `pd.to_datetime(...)` ([CFORPRO](https://www.cforpro.com/formation-python.php?gad_source=1&gad_campaignid=13436643100&gclid=Cj0KCQjw4PPNBhD8ARIsAMo-icxJIrVzrE8UA09lM649JzmYGU5SapWhgejE0kAKAvp27w5KUt7bz2QaApfgEALw_wcB))
- Bonnes pratiques (PEP8, lisibilite, structure de code) ([Cours Python PDF](https://python.sdv.u-paris.fr/cours-python.pdf))

