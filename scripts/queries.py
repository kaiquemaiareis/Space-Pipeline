import sqlite3
import pandas as pd

conn = sqlite3.connect("space.db")

queries = {
    "Quantidade": """
        SELECT COUNT(*) AS total
        FROM asteroids
    """,

    "Magnitude Média": """
        SELECT AVG(absolute_magnitude_h) AS media
        FROM asteroids
    """,

    "Maior Magnitude": """
        SELECT MAX(absolute_magnitude_h) AS maximo
        FROM asteroids
    """,

    "Perigosos": """
        SELECT
            is_potentially_hazardous,
            COUNT(*) AS total
        FROM asteroids
        GROUP BY is_potentially_hazardous
    """
}

for nome, sql in queries.items():

    print(f"\n===== {nome} =====")

    resultado = pd.read_sql(sql, conn)

    print(resultado)

conn.close()