"""
Making a database from CSV file - take 1
"""
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, ForeignKey
import pandas as pd

if __name__ == "__main__":
    ranged_data = pd.read_csv(
        r"CSV/Bronie prototyp - RANGED.csv",
        header=0,
        names=(
            "id_ranged",
            "name",
            "weapon_class",
            "ammo",
            "magazine",
            "misfire_roll",
            "accuracy",
            "shot_range",
            "fire_rate",
            "attack_type",
            "reload",
            "penetration",
            "damage",
            "strength",
            "holster",
            "price",
            "availability",
            "actions",
            "description",
        )
    )
    weapon_data = pd.read_csv(r"CSV/Bronie prototyp - WEAPON.csv")
    ammo_data = pd.read_csv(r"CSV/Bronie prototyp - AMMO.csv")

    ranged_df = pd.DataFrame(
        ranged_data,
        columns=[
            "id_ranged",
            "name",
            "weapon_class",
            "ammo",
            "magazine",
            "misfire_roll",
            "accuracy",
            "shot_range",
            "fire_rate",
            "attack_type",
            "reload",
            "penetration",
            "damage",
            "strength",
            "holster",
            "price",
            "availability",
            "actions",
            "description",
        ],
    )

    weapon_df = pd.DataFrame(
        weapon_data,
        columns=[
            "ID",
            "ID code",
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
            "Modifier 1000m",
            "Modifier 1500m",
        ],
    )

    ammo_df = pd.DataFrame(
        ammo_data,
        columns=[
            "ID",
            "Ammo Symbol",
            "Name",
            "Price",
            "Availability",
            "Crafting Difficulty",
            "Description",
            "Effect",
            "Image",
            "Weight",
        ],
    )
    # Database segment:
    engine = create_engine(
        "sqlite:///C:\\Python_Kurs\\Neuroshima\\database\\main_database.db", echo=True
    )
    meta = MetaData()
    connection = engine.connect()

    ranged = Table(
        "Ranged",
        meta,
        Column("id_ranged", Integer, primary_key=True, autoincrement=True),
        Column("name", String(length=20)),
        Column("weapon_class", String, ForeignKey("Weapon.ID code"), unique=True),
        Column("ammo", Integer, ForeignKey("Ammo.Ammo Symbol"), unique=True),
        Column("magazine", Integer),
        Column("misfire_roll", Integer),
        Column("accuracy", Integer),
        Column("shot_range", Integer),
        Column("fire_rate", Integer),
        Column("attack_type", String(length=20)),
        Column("reload", String(length=20)),
        Column("penetration", Integer),
        Column("damage", String(length=20)),
        Column("strength", Integer),
        Column("holster", Boolean),
        Column("price", Integer),
        Column("availability", Integer),
        Column("actions", String(length=20)),
        Column("description", String(length=20))
    )

    weapon = Table(
        "Weapon",
        meta,
        Column("ID", Integer, primary_key=True, autoincrement=True),
        Column("ID code", String(length=25), unique=True),
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

    ammo = Table(
        "Ammo",
        meta,
        Column("ID", Integer, primary_key=True, autoincrement=True),
        Column("Ammo Symbol", String(length=25), unique=True),
        Column("Name", String(length=50)),
        Column("Price", Integer),
        Column("Availability", Integer),
        Column("Crafting Difficulty", String(length=25)),
        Column("Description", String(length=400)),
        Column("Effect", String(length=50)),
        Column("Image", String(length=50)),
        Column("Weight", Integer),
    )

    meta.create_all(engine)

    # Inserting values from CSV into Table:
    ranged_df.to_sql("Ranged", con=connection, schema=None, if_exists="replace", index=False)
    weapon_df.to_sql("Weapon", con=connection, schema=None, if_exists="replace", index=False)
    ammo_df.to_sql("Ammo", con=connection, schema=None, if_exists="replace", index=False)
