import pandas as pd
import os

# File import
fichier = "phase2/data/sncf.csv"
if not os.path.exists(fichier):
    raise FileNotFoundError(f"Fichier introuvable : {fichier}")

# Reading the CSV file
# Using utf-8-sig to handle BOM and parse dates
df = pd.read_csv("phase2/data/sncf.csv", sep=";", encoding="utf-8-sig", parse_dates=["Date"])
print("Chargement du fichier réussi.")

# Cleaning up column names
df.columns = df.columns.str.strip()

# Cleaning up string columns
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()
    
print("Nettoyage effectué. Colonnes :", df.columns.tolist())
print(df.head())

print("Colonnes finales :", df.columns.tolist())
print(df.info())
print("Valeurs manquantes :\n", df.isnull().sum())

# Top 10 stations by total amount from last 6 months
date_max = df["Date"].max()
date_limite = date_max - pd.DateOffset(months=6)

df_recent = df[df["Date"] >= date_limite]
df["Type jour"] = df["Type jour"].str.strip()

# Filter for working days
df_ouvres = df_recent[df_recent["Type jour"] == "JOB"]
print(f"Période analysée : {date_limite.date()} → {date_max.date()}")
print(f"Nombre de lignes après filtre : {len(df_ouvres)}")
print(df_ouvres.head())

# Unique values in "Type jour"
print(df["Type jour"].unique())

# Display top 10 stations by total amount
top_10_gares = (
    df_ouvres.groupby("Nom Gare")["Somme de Montants"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("Top 10 gares par montant total (jours ouvrés, 6 derniers mois) :")
print(top_10_gares)

# Filter for top 10 stations
top_10_indices = top_10_gares.index.tolist()
df_top10 = df_ouvres[df_ouvres["Nom Gare"].isin(top_10_indices)]

# Calculate average traffic by time slot for top 10 stations
trafic_par_horaire = (
    df_top10.groupby(["Nom Gare", "Tranche horaire"])["Somme de Montants"]
    .mean()
    .reset_index()
    .sort_values(["Nom Gare", "Somme de Montants"], ascending=[True, False])
)

print("Trafic moyen par tranche horaire pour les top 10 gares :")
print(trafic_par_horaire.head(20))  # Display first 20 rows for brevity

# TOP 10 stations by total amount
top_10_gares = (
    df_ouvres.groupby("Nom Gare")["Somme de Montants"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# Filter the DataFrame for top 10 stations
df_top10 = df_ouvres[df_ouvres["Nom Gare"].isin(top_10_gares.index)]

# Calculate average traffic by time slot for top 10 stations
trafic_horaire = (
    df_top10.groupby(["Nom Gare", "Tranche horaire"])["Somme de Montants"]
    .mean()
    .reset_index()
    .sort_values(["Nom Gare", "Somme de Montants"], ascending=[True, False])
)

print(trafic_horaire.head(20))