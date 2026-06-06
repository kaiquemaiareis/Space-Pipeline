import pandas as pd
import os

df = pd.read_csv("data/raw/asteroids_raw.csv")

print("Antes:", len(df))

# Remove linhas vazias
df = df.dropna()

# Converte tipos
df["absolute_magnitude_h"] = pd.to_numeric(
    df["absolute_magnitude_h"],
    errors="coerce"
)

# Padroniza nome
df["name"] = df["name"].astype(str).str.strip()

# Converte booleano para texto
df["is_potentially_hazardous"] = (
    df["is_potentially_hazardous"]
    .astype(str)
)

# Remove nulos gerados na conversão
df = df.dropna()

print("Depois:", len(df))

os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/asteroids_processed.csv",
    index=False
)

print("Arquivo processado criado!")