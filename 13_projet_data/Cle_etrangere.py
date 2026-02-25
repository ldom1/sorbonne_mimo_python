import pandas as pd
import argparse
import os


def verifier_cle_etrangere(fichier_cle, attribut_cle, fichier_etranger):
    # Vérification des fichiers
    if not os.path.exists(fichier_cle):
        print(f"❌ Le fichier maître '{fichier_cle}' n'existe pas.")
        return

    if not os.path.exists(fichier_etranger):
        print(f"❌ Le fichier référent '{fichier_etranger}' n'existe pas.")
        return

    # Lecture des fichiers
    try:
        df_cle = pd.read_csv(fichier_cle, encoding="utf-8")
    except UnicodeDecodeError:
        df_cle = pd.read_csv(fichier_cle, encoding="latin1")

    try:
        df_ref = pd.read_csv(fichier_etranger, encoding="utf-8")
    except UnicodeDecodeError:
        df_ref = pd.read_csv(fichier_etranger, encoding="latin1")

    # Vérification que l'attribut clé existe dans les deux fichiers
    if attribut_cle not in df_cle.columns:
        print(f"❌ La colonne '{attribut_cle}' est absente du fichier clé.")
        return

    if attribut_cle not in df_ref.columns:
        print(f"❌ La colonne '{attribut_cle}' est absente du fichier référent.")
        return

    # Extraction des clés uniques
    cles_valides = set(df_cle[attribut_cle].dropna().unique())
    cles_referencement = df_ref[attribut_cle]

    # Détection des valeurs non référencées
    valeurs_invalides = cles_referencement[~cles_referencement.isin(cles_valides)]

    total = len(cles_referencement)
    nb_invalides = len(valeurs_invalides)
    pourcentage = (nb_invalides / total) * 100 if total > 0 else 0

    print("\n🔍 Résultat de la vérification des clés étrangères :\n")
    print(f"✔️ Total de références vérifiées : {total}")
    print(f"❌ Références non valides : {nb_invalides} ({pourcentage:.2f}%)")

    if nb_invalides > 0:
        print("\n📋 Valeurs non référencées (uniques) :")
        for val in sorted(valeurs_invalides.unique()):
            print(f"   - {val}")

    else:
        print("✅ Toutes les clés étrangères sont valides.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Vérifie l’intégrité des clés étrangères entre deux fichiers CSV"
    )
    parser.add_argument("fichier_cle", help="Fichier contenant les clés primaires")
    parser.add_argument("attribut_cle", help="Nom de la colonne clé")
    parser.add_argument(
        "fichier_etranger", help="Fichier contenant les clés étrangères à valider"
    )

    args = parser.parse_args()
    verifier_cle_etrangere(args.fichier_cle, args.attribut_cle, args.fichier_etranger)
