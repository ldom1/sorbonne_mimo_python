# Chapitre 8 - Programmation Oriente Objet (POO) (notes pour slide)

## Les classes
- Une `class` definit un "modele" pour creer des objets.
- Syntaxe: `class NomClasse: ...`

## Attributs: classe vs instance
- Attribut de classe: definie dans le corps de la classe (partage par les instances).
- Attribut d'instance: definie pour chaque objet, souvent dans `__init__`.

## Constructeur: `__init__`
- `def __init__(self, ...):` initialise l'objet lors de la creation.

## Methodes
- Methode normale: `def methode(self, ...):`
- Appel: `obj.methode(...)`

## Methodes specifiques (dunder methods)
- `__str__`: representation lisible (print)
- `__repr__`: representation "debug"
- `__len__`: `len(obj)`
- `__getitem__`: indexation `obj[i]`
- Operateur surcharge (ex): `__add__`, `__mul__` pour `obj1 + obj2`, `obj1 * obj2`

## Heritage et `super()`
- Une classe peut heriter d'une autre: `class Fille(Parent): ...`
- `super()` pour reutiliser/etendre le comportement parent.

## Polymorphisme
- Le code peut appeler des methodes sur des objets differents (meme nom, comportements differents).

## Potentiel ajout (avec le lien correspondant)
- Classes abstraites via `abc` (ex: `ABC`, `@abstractmethod`) ([CFORPRO](https://www.cforpro.com/formation-python.php?gad_source=1&gad_campaignid=13436643100&gclid=Cj0KCQjw4PPNBhD8ARIsAMo-icxJIrVzrE8UA09lM649JzmYGU5SapWhgejE0kAKAvp27w5KUt7bz2QaApfgEALw_wcB))
- Dataclasses via `@dataclass` pour reduire le code boilerplate ([CFORPRO](https://www.cforpro.com/formation-python.php?gad_source=1&gad_campaignid=13436643100&gclid=Cj0KCQjw4PPNBhD8ARIsAMo-icxJIrVzrE8UA09lM649JzmYGU5SapWhgejE0kAKAvp27w5KUt7bz2QaApfgEALw_wcB))
- `__slots__` pour limiter les attributs et economiser de la memoire ([Cours Python PDF](https://python.sdv.u-paris.fr/cours-python.pdf))
- Methodes de classe (`@classmethod`) et static (`@staticmethod`) ([OpenClassrooms](https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python))
- Verification de type: `isinstance()` / `issubclass()` ([Cours Python PDF](https://python.sdv.u-paris.fr/cours-python.pdf))

