import sqlite3
import pandas as pd

conn = sqlite3.connect("space.db")

df = pd.read_sql(
    "SELECT * FROM asteroids LIMIT 5",
    conn
)

print(df)

conn.close()