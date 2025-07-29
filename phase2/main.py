import pandas as pd
import os

fichier = "phase2/data/sncf.csv"
if not os.path.exists(fichier):
    raise FileNotFoundError(f"Fichier introuvable : {fichier}")

df = pd.read_csv("phase2/data/sncf.csv", sep=";", encoding="utf-8-sig", parse_dates=["Date"])
df.columns = df.columns.str.strip()
print("Chargement du fichier réussi.")
df.info()
df.isnull().sum()
df.columns = df.columns.str.strip()  # Supprime les espaces
print("Colonnes disponibles :", df.columns.tolist())

print(df.head())

top_gares = df.groupby("Nom Gare")["Somme de Montants"].sum().sort_values(ascending=False).head(10)
print("Top 10 gares par montant total :")
print(top_gares)

print(df["Type jour"].unique())
print(df["Tranche horaire"].unique())

montant_par_annee = df.groupby("Annee")["Somme de Montants"].sum()
print(montant_par_annee)

df["Mois"] = df["Date"].dt.to_period("M")
montant_par_mois = df.groupby("Mois")["Somme de Montants"].sum()
print(montant_par_mois.tail(12))
