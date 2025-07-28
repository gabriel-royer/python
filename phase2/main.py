import pandas as pd
import os

fichier = "phase2/data/sncf.csv"
if not os.path.exists(fichier):
    raise FileNotFoundError(f"Fichier introuvable : {fichier}")

df = pd.read_csv("phase2/data/sncf.csv", sep=";", parse_dates=["Date"])
df.info()
df.isnull().sum()
df.columns = df.columns.str.strip()  # Supprime les espaces
print("Colonnes disponibles :", df.columns.tolist())

print(df.head())

top_gares = df.groupby("\ufeffNom Gare")["Somme de Montants"].sum().sort_values(ascending=False).head(10)
print("Top 10 gares par montant total :")
print(top_gares)