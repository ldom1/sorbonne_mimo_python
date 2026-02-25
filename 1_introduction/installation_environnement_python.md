# Installation de l'environnement Python

Ce document décrit l'installation de Python et de **uv** (gestionnaire de projets et de paquets) sur Windows, macOS et Linux, puis la création d'un projet et d'un environnement virtuel.

---

## Qu'est-ce qu'un environnement virtuel ?

Un **environnement virtuel** est un espace isolé qui contient un interpréteur Python et des paquets (bibliothèques) propres à un projet. Cela permet :

- d'avoir des **versions de paquets différentes** selon les projets sans conflit ;
- de **reproduire** exactement le même environnement (mêmes versions) sur une autre machine ;
- de ne pas polluer l'installation Python globale du système.

**Attendu** : à la fin du setup, vous devez avoir un dossier de projet avec un fichier `pyproject.toml`, un environnement virtuel (dossier `.venv`) et pouvoir lancer du code avec `uv run python script.py` ou `uv run jupyter lab`.

---

## Installation de uv

### Windows

**PowerShell** :

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Après installation, vérifiez : `uv --version`. Si la commande n’est pas trouvée, redémarrez le terminal ou ajoutez `%USERPROFILE%\.local\bin` à la variable d’environnement `PATH`.

---

### macOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Ou avec **Homebrew** :

```bash
brew install uv --formula
```

Vérifiez : `uv --version`. Si besoin, le script d’installation indique comment ajouter `~/.local/bin` à votre `PATH` (souvent dans `~/.zshrc` ou `~/.bash_profile`).

---

### Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Vérifiez : `uv --version`. Ajoutez éventuellement `~/.local/bin` à votre `PATH` dans `~/.bashrc` ou `~/.zshrc` :

```bash
export PATH="$HOME/.local/bin:$PATH"
```

---

## Créer un projet et un environnement virtuel avec uv

### 1. Créer un nouveau projet

Dans un nouveau dossier :

```bash
mkdir mon_projet
cd mon_projet
uv init
```

Ou en une ligne :

```bash
uv init mon_projet
cd mon_projet
```

Cela crée notamment :

- `pyproject.toml` (configuration et dépendances du projet)
- `.python-version` (version de Python cible)
- un fichier d’exemple (ex. `main.py`)

### 2. Créer / utiliser l’environnement virtuel

uv crée automatiquement un environnement virtuel (dossier `.venv`) dès que vous exécutez une commande du projet, par exemple :

```bash
uv sync
```

Pour créer explicitement le `.venv` sans installer les dépendances :

```bash
uv venv
```

### 3. Installer des dépendances

Ajouter un paquet (ex. `jupyter`) :

```bash
uv add jupyterlab
```

Installer toutes les dépendances du `pyproject.toml` (et mettre à jour le fichier de lock) :

```bash
uv sync
```

### 4. Lancer du code

Exécuter un script dans l’environnement du projet :

```bash
uv run python main.py
```

Lancer Jupyter Lab :

```bash
uv run jupyter lab
```

---

## Récapitulatif

| Étape              | Commande (exemple)        |
|--------------------|---------------------------|
| Installer uv       | Voir section selon l’OS   |
| Créer un projet    | `uv init mon_projet`      |
| Aller dans le projet | `cd mon_projet`          |
| Créer / mettre à jour l’env | `uv sync`        |
| Ajouter un paquet  | `uv add numpy`            |
| Exécuter un script | `uv run python main.py`   |

**Attendu final** : projet avec `pyproject.toml`, environnement virtuel `.venv`, et commandes `uv run` fonctionnelles.
