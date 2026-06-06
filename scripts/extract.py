import requests
import pandas as pd
import os

url = "https://api.nasa.gov/neo/rest/v1/feed?api_key=DEMO_KEY"

response = requests.get(url, timeout=30)

data = response.json()

asteroids = []

for date in data["near_earth_objects"]:

    for asteroid in data["near_earth_objects"][date]:

        asteroids.append({
            "id": asteroid["id"],
            "name": asteroid["name"],
            "absolute_magnitude_h": asteroid["absolute_magnitude_h"],
            "is_potentially_hazardous":
                asteroid["is_potentially_hazardous_asteroid"]
        })

df = pd.DataFrame(asteroids)

os.makedirs("data/raw", exist_ok=True)

df.to_csv(
    "data/raw/asteroids_raw.csv",
    index=False
)

print(df.head())
print(f"\nTotal de registros: {len(df)}")