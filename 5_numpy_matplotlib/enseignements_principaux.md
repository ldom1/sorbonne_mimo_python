# Chapitre 5 - NumPy et Matplotlib (notes pour slide)

## NumPy
- Difference: `list` vs `numpy.ndarray` (operations vectorisees)
- Import: `import numpy as np`

### 1. Creer un array
- `np.array([...])`
- `np.arange(start, stop, step)` (ou sans `start`)
- `np.zeros((n, m))`, `np.ones((n, m))`, `np.full((n, m), v)`
- Arrays multi-dimensions: `shape`, indexation `[i, j, ...]`

### 2. Operations sur les arrays
- Operations element par element: `a + b`, `a * 2`, `a / b`, etc.
- Transpose: `.T` (selon dimensions)
- Dot produit: `np.dot(a, b)` (ou `@` selon cas)

### 3. Reshape
- `a.reshape(new_shape)` pour changer la forme (nombre d'elements identique)

### 4. Indexation
- Indexation 1D/2D: `a[i]`, `a[i, j]`
- Slicing: `a[i:j, k:l]`

### 5. Fonctions calculatoires/statistiques
- Exemples typiques: `np.sum`, `np.mean`, `np.min`, `np.max`, `np.std`

### 6. Masques (filtrage)
- Principe: creer un masque booleen puis indexer
  - ex: `a[a > 0]`
- Variantes: masque sur lignes/colonnes, filtrage conditionnel

### Pour aller plus loin: Broadcasting
- Rendre compatibles des shapes differentes pour operations (regles de diffusion)

## Matplotlib
- Import: `import matplotlib.pyplot as plt`

### 1. Graphiques simples
- `plt.plot(x, y)` (courbe)
- `plt.scatter(x, y)` (nuage de points)
- `plt.bar(x, y)` (barres)

### 2. Types de graphiques (a retenir)
- Courbes / points (et leurs variantes)
- Histogrammes / barres

### 3. Personnalisation
- Titres et axes: `plt.xlabel`, `plt.ylabel`, `plt.title`
- Limites: `plt.xlim`, `plt.ylim`
- Legend: `plt.legend()`
- Grille: `plt.grid(True)`

### 4. Sous-graphiques
- `plt.figure()`, puis `plt.subplot(...)` pour plusieurs vues

### 5. Enregistrement
- `plt.savefig("figure.png")` puis (souvent) `plt.show()`

## Potentiel ajout (avec le lien correspondant)
- Importation/alias de modules pour integrer `numpy` / `matplotlib` proprement dans ses scripts ([OpenClassrooms](https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python))
- Installation de bibliotheques via `pip` pour ajouter `numpy/matplotlib` si besoin ([CFORPRO](https://www.cforpro.com/formation-python.php?gad_source=1&gad_campaignid=13436643100&gclid=Cj0KCQjw4PPNBhD8ARIsAMo-icxJIrVzrE8UA09lM649JzmYGU5SapWhgejE0kAKAvp27w5KUt7bz2QaApfgEALw_wcB))
- Bonnes pratiques (PEP8, lisibilite) pour structurer un notebook/script scientifique ([Cours Python PDF](https://python.sdv.u-paris.fr/cours-python.pdf))

