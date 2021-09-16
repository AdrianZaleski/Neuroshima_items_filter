"""
Making a database from CSV file - take 1
"""

import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean

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

    # Preparation for database and first table:
    engine = create_engine("sqlite:///C:\\Python_Kurs\\Neuroshima\\database\\main_database2.db", echo=True)
    meta = MetaData()
    connection = engine.connect()

    ranged = Table(
        "Ranged",
        meta,
        Column("ID", Integer, primary_key=True, autoincrement=True),
        Column("Name", String(length=20)),
        Column("Weapon Class", String(length=20)),
        Column("Ammo_id", String(length=20)),
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
    meta.create_all(engine)
