import pandas as pd
import sqlite3

df = pd.read_csv(
    "data/processed/asteroids_processed.csv"
)

conn = sqlite3.connect("space.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS asteroids (
    id TEXT,
    name TEXT,
    absolute_magnitude_h REAL,
    is_potentially_hazardous TEXT
)
""")

df.to_sql(
    "asteroids",
    conn,
    if_exists="append",
    index=False
)

conn.commit()

print(f"{len(df)} registros carregados!")

conn.close()