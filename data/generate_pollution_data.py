import csv
from datetime import datetime, timedelta
import random

# Définition des villes et polluants
villes = ["Paris", "Lyon", "Marseille", "Toulouse"]
polluants = ["NO2", "O3", "PM10", "SO2"]
start_date = datetime(2023, 1, 1)

# Création du fichier CSV
with open("pollution_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["date", "ville", "polluant", "valeur"])
    for i in range(100): # 100 jours
        date = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
        for ville in villes:
            for polluant in polluants:
                valeur = round(random.uniform(10, 100), 2)
                writer.writerow([date, ville, polluant, valeur])