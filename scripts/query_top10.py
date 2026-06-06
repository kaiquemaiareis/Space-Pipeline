import sqlite3
import pandas as pd

conn = sqlite3.connect("space.db")

df = pd.read_sql("""
SELECT
    name,
    absolute_magnitude_h
FROM asteroids
ORDER BY absolute_magnitude_h DESC
LIMIT 10
""", conn)

print(df)

conn.close()