"""
 la boucle d’analyse,  :
ne supprime pas les valeurs manquantes (.dropna() supprimé)
remplace les NaN par une étiquette explicite ("Non renseigné")
affiche les pourcentages y compris pour ces valeurs
avec un tri explicite en ordre croissant des étiquettes de valeur
des colonnes à exclure sont passées en argument au script
avec option --top pour limiter le nombre de valeurs affichées par colonne
— par exemple --top 10 pour n’afficher que les 10 valeurs les plus fréquentes,

.venv\Scripts\python analyse_valeurs.py --exclude Num_Acc hrmn com adr gps lat long "C:\Georges\Fac\Mimo\Cours\Cours Gestion de la Donnée\Travaux Pratiques\Données\accidents_TP\base\caracteristiques_2005.csv"

"""

import os
import pandas as pd
import argparse
import matplotlib.pyplot as plt


def analyser_colonnes(chemin_fichier, colonnes_a_exclure, top_n=None):
    if not os.path.isfile(chemin_fichier):
        print(f"❌ Le fichier '{chemin_fichier}' n'existe pas.")
        return

    try:
        df = pd.read_csv(
            chemin_fichier, encoding="utf-8", delimiter=",", low_memory=False
        )
    except UnicodeDecodeError:
        df = pd.read_csv(
            chemin_fichier, encoding="latin1", delimiter=",", low_memory=False
        )

    if df.columns.size == 0:
        print("❌ Aucune colonne détectée dans le fichier.")
        return

    colonnes_utiles = [col for col in df.columns if col not in colonnes_a_exclure]

    # Dossier de sortie des graphiques
    dossier_graphiques = "graphiques"
    os.makedirs(dossier_graphiques, exist_ok=True)

    print("📊 Analyse des colonnes avec génération de camemberts :\n")

    for col in colonnes_utiles:
        print(f"🔹 Colonne : {col}")

        try:
            series = pd.to_numeric(df[col], errors="coerce").fillna("Non renseigné")
            counts = series.value_counts()

            # Fonction de tri pour mettre les valeurs dans l'ordre
            def tri_personnalise(val):
                if val == "Non renseigné":
                    return float("inf")
                return (
                    float(val) if str(val).replace(".", "", 1).isdigit() else str(val)
                )

            counts = counts.sort_index(key=lambda x: x.map(tri_personnalise))

            if top_n is not None and top_n > 0:
                counts = counts.head(top_n)

            total = series.shape[0]

            for val, count in counts.items():
                pourcentage = (count / total) * 100
                print(f"   {str(val):>15} → {count:>6} ligne(s) → {pourcentage:6.2f} %")

            # 🔵 Génération du camembert
            labels = [str(v) for v in counts.index]
            sizes = [v for v in counts.values]

            plt.figure(figsize=(6, 6))
            plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
            plt.axis("equal")  # égaliser les axes pour un vrai cercle
            plt.title(f"Répartition des valeurs - {col}")

            # Sauvegarde du graphique
            chemin_sortie = os.path.join(dossier_graphiques, f"{col}.png")
            plt.savefig(chemin_sortie)
            print(f"   ✅ Image générée pour la colonne : {col}")
            plt.close()

            print(f"   📁 Camembert enregistré : {chemin_sortie}\n")

        except Exception as e:
            print(f"   ⚠️ Erreur pendant le traitement de la colonne '{col}' : {e}")

        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyse de colonnes d’un fichier CSV")
    parser.add_argument("fichier", help="Chemin vers le fichier CSV à analyser")
    parser.add_argument(
        "--exclude",
        nargs="*",
        default=[],
        help="Noms des colonnes à exclure (séparés par un espace)",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=None,
        help="Nombre maximum de valeurs à afficher par colonne (ex : --top 10)",
    )

    args = parser.parse_args()
    analyser_colonnes(args.fichier, args.exclude, args.top)
