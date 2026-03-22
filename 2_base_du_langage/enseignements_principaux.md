# Chapitre 2 - Bases du langage Python (notes pour slide)

## Idee generale
- Python: langage interprete, type dynamique (pas besoin de declarer le type).
- Indentation significative pour les blocs (if/for/while/def, etc.).
- La base de l'interaction: la `variable` (un conteneur).
- Commentaires: prefixe `#` + espace.

## Syntaxe: variables, affectations, affichage
- Affectation: `nom = valeur`
- Multi-affectation: `a, b = 1, 2`
- Affectation augmentee: `x += 1`, `x -= 1`, etc.
- Sensibilite a la casse: `var != VAR != Var`
- Type et identite:
  - `type(var)`
  - `id(var)` (identite memoire)
- Affichage: `print(...)` (ex: `print(x, end="")`)
- Lecture: `input("prompt")` (retourne toujours un `str`)
- Conversion (casting): `int(...)`, `float(...)`, `str(...)`, `list(...)`, `tuple(...)`, `set(...)`, `dict(...)`, `bool(...)`

## Types de donnees (vues)
- `None` (valeur nulle / absence)
- Booleens: `True` / `False`
- Numeriques: `int`, `float`, `complex` (ex: `1j`)
- `str` (chaines)
- Sequences (indexation):
  - `list` (modifiable)
  - `tuple` (immutable)
  - indexation a partir de `0` et indices negatifs (`s[-1]`)
- `dict` (cle -> valeur)
- `set` (elements uniques, non ordonne)
- `frozenset` (set immutable)

## Numerique: operateurs et comparaisons
- Arithmetic: `+ - * / // % **`
- Comparaison (donne un `bool`): `== != < > <= >=`
- Ordre (priorite) des operateurs: utiliser des parentheses quand ce n'est pas evident.

## Booleens et logique
- Operateurs: `not`, `and`, `or`
- Priorite: `not` > `and` > `or`
- Court-circuit:
  - `A or B`: `B` seulement si necessaire
  - `A and B`: `B` seulement si necessaire
- Regle cle `bool(...)`:
  - `False`: `None`, `0`, `""`, collections vides
  - `True`: sinon

## Chaines de caracteres (`str`)
- Delimiteurs: `"..."`, `'...'`, `"""..."""`, `'''...'''`
- Indexation: `s[i]`
- Slicing: `s[start:stop:step]`
- Operations:
  - concatener: `a + b`
  - repetition: `c * 2`
- Formatage:
  - operateur `%` (style `printf`)
  - methode `.format()`
  - f-strings: `f"texte {var}"`
- Methodes utiles (souvent vues au debut):
  - `s.lower()`, `s.upper()`
  - `s.strip()`
  - `s.split(sep)`
  - `s.replace(old, new)`
  - `sep.join(iterable)`

## Listes et tuples
- Acces: `lst[i]` (et `lst[i][j]` si imbrique)
- Tranches: `lst[i:j]`
- Liste (modifiable): `append`, `extend`, `insert`, `remove`, `del`, `pop`
- Tri/ordre: `sort`, `reverse`
- Informations: `len`, `count`, `index`, `in`
- Tuple: immutable, pratique pour valeurs fixes + deconstruction.

## Dictionnaires (`dict`)
- Definition: `{"cle": valeur, ...}`
- Acces:
  - `d["cle"]` (KeyError si absent)
  - `d.get("cle", default)` (plus sure)
- Ajout / modification: `d["nouvelle_cle"] = valeur`, `d.update({...})`
- Suppression: `del d["cle"]`, `d.pop("cle")`
- Parcours / vues:
  - `d.keys()`, `d.values()`, `d.items()`

## Ensembles (`set`) et `frozenset`
- Creation: `set(iterable)` pour dedoublonner
- Tests d'appartenance: `x in s`
- Operations:
  - union `|`, intersection `&`
  - difference `-`
  - symetrique `^`
- Methodes: `add`, `discard` (pas d'erreur si absent), `remove`

## Builtins utilies (debuts)
- `len`, `sum`, `min`, `max`, `sorted`
- `range(stop)` / `range(start, stop, step)`
- `enumerate(iterable)` (indices + valeurs)
- `zip(a, b)` (paires)
- `map(f, iterable)` (application)
- `isinstance(x, type)` (controle type)
- `hasattr(obj, "attr")` (controle attribut)
- `divmod(a, b)` -> `(quotient, reste)`
- `chr(n)` (code -> caractere), `ord(c)` (caractere -> code)

## Modules, imports (packages natifs)
- `import math` puis `math.sqrt`, `math.pi`
- `import random` puis `random.randint(a, b)`
- `from random import randint as rint` (alias)

## Fichiers
- Ecrire:
  - `with open(file_path, "w", encoding="utf-8") as f: f.write(...)`
- Lire:
  - `with open(file_path, "r", encoding="utf-8") as f: contenu = f.read()`
- Bonus pratique: iterer ligne par ligne (`for line in f:`) pour gros fichiers.

## Potentiel ajout (avec le lien correspondant)
- [OpenClassrooms](https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python): installation/usage de packages et logique de programme avec conditions, boucles, fonctions; extraction web via packages `Requests`, `Beautiful Soup`, `CSV`.
- [NSI - PriseEnMainPython](https://cours-nsi.forge.apps.education.fr/premiere/PriseEnMainPython.html): prise en main via environnements (notebooks Jupyter, `EduPyter`, `Capytale`) et execution dans une console.
- [CFORPRO](https://www.cforpro.com/formation-python.php?gad_source=1&gad_campaignid=13436643100&gclid=Cj0KCQjw4PPNBhD8ARIsAMo-icxJIrVzrE8UA09lM649JzmYGU5SapWhgejE0kAKAvp27w5KUt7bz2QaApfgEALw_wcB): Python comme langage interprete + bonnes pratiques (PEP8: indentation, code layout, espaces, commentaires).
- [Cours Python PDF](https://python.sdv.u-paris.fr/cours-python.pdf): regle PEP8 "4 espaces par niveau" et commentaires `#` suivis d'un espace pour un code lisible.

