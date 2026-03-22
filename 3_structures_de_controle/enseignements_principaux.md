# Chapitre 3 - Les structures de controle (notes pour slide)

## Introduction
- Les structures de controle pilotent le deroulement: decisions (`if/match`) et repetitions (`for/while`).
- Tout repose sur l'indentation et des conditions qui evaluent en `bool`.

## Notions fondamentales
- Conditionnelle: `if`, `elif`, `else`
- Alternative (Python 3.10+): `match/case`
- Boucles:
  - `for` sur un iterable
  - `while` sur une condition
- Controle de boucle: `break`, `continue`
- Outils pratiques: `range`, `enumerate`, `zip`

## Conditionnel: `if / elif / else`
- Syntaxe:
  - `if condition: ...`
  - `elif condition: ...`
  - `else: ...`
- `condition` peut etre une expression de comparaison (`x > 3`) ou une combinaison logique (`and/or/not`).

## `match / case` (Python 3.10+)
- Syntaxe generale:
  - `match x:`
  - `  case valeur: ...`
  - `  case autre_valeur | alias: ...`
  - `  case _: ...` (cas par defaut)
- Variante utile: garde (`case pattern if condition:`) pour affiner.

## Boucles

### Boucle `while`
- Syntaxe: `while condition: ...`
- Attention: mettre a jour la condition pour eviter une boucle infinie.
- Optionnel (Python): `else` sur `while` s'execute si la boucle finit naturellement (pas de `break`).

### Boucle `for`
- Syntaxe: `for var in iterable: ...`
- Cas frequents:
  - `for i in range(...)`
  - `for el in liste`
  - iteration sur un `dict` (par defaut: cles)
- Optionnel (Python): `else` sur `for` s'execute si la boucle finit naturellement (pas de `break`).

## Controle de boucle: `break` et `continue`
- `break`: arrete immediatement la boucle.
- `continue`: saute le reste de l'iteration courante et passe a la suivante.

## `range`, `enumerate` et `zip`
- `range(stop)` / `range(start, stop, step)` pour generer des entiers.
- `enumerate(iterable, start=0)` retourne `(index, valeur)`.
- `zip(a, b, ...)` associe les elements (s'arrete a la longueur la plus courte).

## Methodes standard de listes (rappel)
- `append`, `extend`, `insert`, `remove`, `pop`, `clear`
- `sort`, `reverse`
- `count`, `index`

## Potentiel ajout (avec le lien correspondant)
- Expression conditionnelle (ternaire): `x if cond else y` ([OpenClassrooms](https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python))
- `else` de boucle (`for/while ... else`) pour differencier "termine" vs "interrompu par `break`" ([OpenClassrooms](https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python))
- `nested loops` (boucles imbriquees) pour explorer des combinaisons (ex: systeme de recommandation, decoupage de grilles) ([CFORPRO](https://www.cforpro.com/formation-python.php?gad_source=1&gad_campaignid=13436643100&gclid=Cj0KCQjw4PPNBhD8ARIsAMo-icxJIrVzrE8UA09lM649JzmYGU5SapWhgejE0kAKAvp27w5KUt7bz2QaApfgEALw_wcB))
- Mot-cle `pass` pour creer un bloc vide temporaire ([CFORPRO](https://www.cforpro.com/formation-python.php?gad_source=1&gad_campaignid=13436643100&gclid=Cj0KCQjw4PPNBhD8ARIsAMo-icxJIrVzrE8UA09lM649JzmYGU5SapWhgejE0kAKAvp27w5KUt7bz2QaApfgEALw_wcB))

