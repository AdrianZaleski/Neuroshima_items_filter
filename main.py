"""
Making a database from CSV file - take 1
"""

import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, ForeignKey

if __name__ == "__main__":
    ranged_data = pd.read_csv(r"CSV/Bronie prototyp - RANGED.csv")
    weapon_data = pd.read_csv(r"CSV/Bronie prototyp - WEAPON.csv")

    ranged_df = pd.DataFrame(
        ranged_data,
        columns=[
            "ID",
            "Name",
            "Weapon Class",
            "Ammo",
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
        ],
    )

    weapon_df = pd.DataFrame(
        weapon_data,
        columns=[
            "ID",
            "Name",
            "Description",
            "Modifier 10m",
            "Modifier 20m",
            "Modifier 30m",
            "Modifier 40m",
            "Modifier 60m",
            "Modifier 80m",
            "Modifier 100m",
            "Modifier 100m",
            "Modifier 150m",
            "Modifier 200m",
            "Modifier 250m",
            "Modifier 300m",
            "Modifier 400m",
            "Modifier 600m",
            "Modifier 1000m"
            "Modifier 1500m",
        ],
    )
    print(weapon_df)
    # Preparation for database and first table:
    engine = create_engine(
        "sqlite:///C:\\Python_Kurs\\Neuroshima\\database\\main_database.db", echo=True
    )
    meta = MetaData()
    connection = engine.connect()

    ranged = Table(
        "Ranged",
        meta,
        Column("ID", String(length=20), primary_key=True, unique=True),
        Column("Name", String(length=20)),
        Column("Weapon_Class", String(length=20), ForeignKey("Weapon.ID")),
        Column("Ammo", String(length=20)),
        Column("Magazine", Integer),
        Column("Misfire roll", Integer),
        Column("Celność w %", Integer),
        Column("Zasięg [m]", Integer),
        Column("Fire Rate", Integer),
        Column("Attack Type", String(length=20)),
        Column("Reload", String(length=20)),
        Column("Punkty przebicia", Integer),
        Column("Damage", String(length=20)),
        Column("Strength", Integer),
        Column("Holster", Boolean),
        Column("Price", Integer),
        Column("Availability", Integer),
        Column("Actions", String(length=20)),
        Column("Description", String(length=20)),
    )

    weapon = Table(
        "Weapon",
        meta,
        Column("ID", String(length=20), primary_key=True, unique=True),
        Column("Name", String(length=25)),
        Column("Description", String(length=400)),
        Column("Modifier 10m", Integer),
        Column("Modifier 20m", Integer),
        Column("Modifier 30m", Integer),
        Column("Modifier 40m", Integer),
        Column("Modifier 60m", Integer),
        Column("Modifier 80m", Integer),
        Column("Modifier 100m", Integer),
        Column("Modifier 100m", Integer),
        Column("Modifier 150m", Integer),
        Column("Modifier 200m", Integer),
        Column("Modifier 250m", Integer),
        Column("Modifier 300m", Integer),
        Column("Modifier 400m", Integer),
        Column("Modifier 600m", Integer),
        Column("Modifier 1000m", Integer),
        Column("Modifier 1500m", Integer),
    )

    meta.create_all(engine)

    # Inserting values from CSV into Table:
    ranged_df.to_sql("Ranged", con=connection, schema=None, if_exists="replace", index=False)
    weapon_df.to_sql("Weapon", con=connection, schema=None, if_exists="replace", index=False)
