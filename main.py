"""
Making a database from CSV file - take 1
"""

import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv(r"CSV/Bronie prototyp - RANGED.csv")
    df = pd.DataFrame(
        data,
        columns=[
            "ID",
            "Name",
            "Weapon Class",
            "Ammo_id",
            "Magazine",
            "Misfire roll",
            "Celność w %",
            "Zasięg [m]",
            "Fire Rate",
            "Attack Type",
            "Reload",
            "Punkty przebicia",
            "Damage",
            "Strength",
            "Holster",
            "Price",
            "Availability",
            "Actions",
            "Description",
        ]
    )
    print(df)

