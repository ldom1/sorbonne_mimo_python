# Chapitre 4 - Les fonctions (notes pour slide)

## Pourquoi utiliser les fonctions
- Regrouper une logique: reutiliser, clarifier, factoriser (`DRY`).
- Separer les responsabilites (une fonction fait une chose).

## Creer une fonction: `def`
- Definition:
  - `def nom(param1, param2=valeur_par_defaut, ...):`
  - `  ...`
  - `  return resultat`
- Appel: `nom(arg1, arg2, ...)`

## Arguments: positionnels vs nommes
- Positionnels: `f(1, 2)`
- Nomme: `f(x=1, y=2)` (lisibilite)
- Pourquoi: evite les erreurs et rend le code plus explicite.

## Typer les arguments (type hints) et docstring
- Type hints: `def f(x: int) -> float: ...`
- Documentation (docstring): `""" ... """` au debut de la fonction.

## Gestion des erreurs dans les fonctions
- Valider les entrees.
- Utiliser `try/except`:
  - gerer une exception precise (ex: `ValueError`, `TypeError`)
  - sinon laisser remonter / `raise`

## Pour aller plus loin: recursion, lambda, generateurs

### Fonctions recursives
- Principe: appel de la fonction sur un sous-probleme.
- Toujours definir un cas de base pour stopper.

### `lambda` (fonction anonyme)
- Syntaxe courte: `lambda args: expression`
- Souvent pour des petites fonctions utilisees inline.

### Generateurs (`yield`)
- Une fonction generator: `yield valeur` pour produire une sequence paresseuse.
- Avantage: iterer sans creer toute la liste en memoire.

## Tests unitaires (idee)
- Tester des fonctions avec des cas "attendus": entree -> sortie.
- Permet de verifier un comportement apres modification.

## Potentiel ajout (avec le lien correspondant)
- Parametres variables: `*args` et `**kwargs` pour accepter un nombre flexible d'arguments ([OpenClassrooms](https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python))
- Valeurs par defaut: attention a la mutabilite (ex: liste en parametre) ([OpenClassrooms](https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python))
- Decorateurs (`@...`) et acces a `__doc__` / documentation via introspection ([CFORPRO](https://www.cforpro.com/formation-python.php?gad_source=1&gad_campaignid=13436643100&gclid=Cj0KCQjw4PPNBhD8ARIsAMo-icxJIrVzrE8UA09lM649JzmYGU5SapWhgejE0kAKAvp27w5KUt7bz2QaApfgEALw_wcB))
- Notion de "fonction recurssive + cas de base" et structuration du code ([CFORPRO](https://www.cforpro.com/formation-python.php?gad_source=1&gad_campaignid=13436643100&gclid=Cj0KCQjw4PPNBhD8ARIsAMo-icxJIrVzrE8UA09lM649JzmYGU5SapWhgejE0kAKAvp27w5KUt7bz2QaApfgEALw_wcB))

