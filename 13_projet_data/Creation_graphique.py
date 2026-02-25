import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

# 📁 Dossier contenant les fichiers CSV
DOSSIER = "Données"

# 🔎 Chargement de tous les fichiers caractéristiques et véhicules
fichiers_carac = sorted(glob.glob(os.path.join(DOSSIER, "caracteristiques_*.csv")))
fichiers_vehic = sorted(glob.glob(os.path.join(DOSSIER, "vehicules_*.csv")))

if not fichiers_carac or not fichiers_vehic:
    print("❌ Aucun fichier caractéristiques ou véhicules trouvé dans le dossier.")
    exit()

# 📘 Dictionnaire des codes catv → libellés (à adapter selon nomenclature exacte)
libelles_catv = {
    0: "Indéterminable",
    1: "Bicyclette",
    2: "Cyclomoteur <50cm3",
    3: "Voiturette (Quadricycle à moteur carrossé) (anciennement voiturette ou tricycle à moteur)",
    4: "Référence inutilisée depuis 2006 (scooter immatriculé)",
    5: "Référence inutilisée depuis 2006 (motocyclette)",
    6: "Référence inutilisée depuis 2006 (side-car)",
    #    7: "VL seul",
    8: "Référence inutilisée depuis 2006 (VL + caravane)",
    9: "Référence inutilisée depuis 2006 (VL + remorque)",
    10: "VU seul 1,5T <= PTAC <= 3,5T avec ou sans remorque (anciennement VU seul 1,5T <= PTAC <= 3,5T)",
    11: "Référence inutilisée depuis 2006 (VU (10) + caravane)",
    12: "Référence inutilisée depuis 2006 (VU (10) + remorque)",
    13: "PL seul 3,5T <PTCA <= 7,5T",
    14: "PL seul > 7,5T",
    15: "PL > 3,5T + remorque",
    16: "Tracteur routier seul",
    17: "Tracteur routier + semi-remorque",
    18: "Référence inutilisée depuis 2006 (transport en commun)",
    19: "Référence inutilisée depuis 2006 (tramway)",
    20: "Engin spécial",
    21: "Tracteur agricole",
    30: "Scooter < 50 cm3",
    31: "Motocyclette > 50 cm3 et <= 125 cm3",
    32: "Scooter > 50 cm3 et <= 125 cm3",
    33: "Motocyclette > 125 cm3",
    34: "Scooter > 125 cm3",
    35: "Quad léger <= 50 cm3 (Quadricycle à moteur non carrossé)",
    36: "Quad lourd > 50 cm3 (Quadricycle à moteur non carrossé)",
    37: "Autobus",
    38: "Autocar",
    39: "Train",
    40: "Tramway",
    41: "3RM <= 50 cm3",
    42: "3RM > 50 cm3 <= 125 cm3",
    43: "3RM > 125 cm3",
    50: "EDP à moteur",
    60: "EDP sans moteur",
    80: "VAE",
    99: "Autre véhicule",
}

# 📊 Accumulateur de toutes les données jointes
df_joint_total = pd.DataFrame()

for fichier_carac, fichier_vehic in zip(fichiers_carac, fichiers_vehic):
    print(
        f"Traitement : {os.path.basename(fichier_carac)} et {os.path.basename(fichier_vehic)}"
    )

    try:
        df_carac = pd.read_csv(fichier_carac, encoding="latin1", delimiter=",")
        df_vehic = pd.read_csv(fichier_vehic, encoding="latin1", delimiter=",")
    except Exception as e:
        print(f"⚠️ Erreur lors du chargement : {e}")
        continue

    if (
        not {"Num_Acc", "an"}.issubset(df_carac.columns)
        or "Num_Acc" not in df_vehic.columns
        or "catv" not in df_vehic.columns
    ):
        print("⚠️ Colonnes manquantes dans les fichiers, passage au suivant.")
        continue

    df_joint = pd.merge(
        df_vehic, df_carac[["Num_Acc", "an"]], on="Num_Acc", how="inner"
    )
    df_joint = df_joint.dropna(subset=["an", "catv"])
    df_joint["an"] = pd.to_numeric(df_joint["an"], errors="coerce").astype("Int64")
    df_joint["catv"] = pd.to_numeric(df_joint["catv"], errors="coerce").astype("Int64")
    df_joint_total = pd.concat([df_joint_total, df_joint], ignore_index=True)

# 🧹 Nettoyage
df_joint_total = df_joint_total.dropna(subset=["an", "catv"])

# 🔤 Remplacement des codes catv par libellés
df_joint_total["catv_libelle"] = (
    df_joint_total["catv"].map(libelles_catv).fillna("Inconnu")
)

# 📈 Comptage par année et type de véhicule
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

df_grouped = df_joint_total.groupby(["an", "catv_libelle"]).size().unstack(fill_value=0)


# 🔁 On reprend df_grouped (index=an, colonnes=catv_libelle)
df_3d = df_grouped.T  # Transposition pour avoir catv_libelle en X et an en Z

# 🔢 Création des coordonnées
x_labels = list(df_3d.index)  # catégories de véhicule
z_labels = list(df_3d.columns)  # années

x_pos, z_pos = np.meshgrid(
    np.arange(len(x_labels)), np.arange(len(z_labels)), indexing="ij"
)
x_pos = x_pos.flatten()
z_pos = z_pos.flatten()
y_pos = np.zeros_like(x_pos)

# 📊 Hauteur des barres (valeurs)
y_values = df_3d.values.flatten()

# Dimensions des barres
dx = dy = 0.8
dz = y_values

# 🎨 Création du graphique 3D
fig = plt.figure(figsize=(18, 10))
ax = fig.add_subplot(111, projection="3d")

ax.bar3d(x_pos, y_pos, z_pos, dx, dz, dy, shade=True, color="skyblue")

# 🏷️ Mise en forme des axes
ax.set_xlabel("Catégorie de véhicule")
ax.set_ylabel("Nombre d'accidents")
ax.set_zlabel("Année")

ax.set_xticks(np.arange(len(x_labels)) + dx / 2)
ax.set_xticklabels(x_labels, rotation=45, ha="right")

ax.set_zticks(np.arange(len(z_labels)) + dy / 2)
ax.set_zticklabels(z_labels)

ax.set_title("Accidents par catégorie de véhicule et par année (graphique 3D)")
plt.tight_layout()

# 💾 Enregistrement
plt.savefig("accidents_vehicules_3D.png")
print("✅ Graphique 3D enregistré : accidents_vehicules_3D.png")

plt.show()
