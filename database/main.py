"""
Making a database from CSV file - take 1
- Using pandas for import data from CSV files with updated headers into main_database.db file

"""
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, ForeignKey


if __name__ == "__main__":
    ranged_data = pd.read_csv(
        r"C:\\Python_Kurs\\Neuroshima\\CSV\\Bronie prototyp - RANGED.csv",
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
    weapon_data = pd.read_csv(
        r"C:\\Python_Kurs\\Neuroshima\\CSV\\Bronie prototyp - WEAPON.csv",
        header=0,
        names=(
            "id_code",
            "name",
            "description",
            "modifier_10m",
            "modifier_20m",
            "modifier_30m",
            "modifier_40m",
            "modifier_60m",
            "modifier_80m",
            "modifier_100m",
            "modifier_150m",
            "modifier_200m",
            "modifier_250m",
            "modifier_300m",
            "modifier_400m",
            "modifier_600m",
            "modifier_1000m",
            "modifier_1500m",
        )

    )
    ammo_data = pd.read_csv(
        r"C:\\Python_Kurs\\Neuroshima\\CSV\\Bronie prototyp - AMMO.csv",
        header=0,
        names=(
            "id_code",
            "ammo_symbol",
            "name",
            "price",
            "availability",
            "crafting_difficulty",
            "description",
            "effect",
            "image",
            "weight",
        )
    )

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
            "id_code",
            "name",
            "description",
            "modifier_10m",
            "modifier_20m",
            "modifier_30m",
            "modifier_40m",
            "modifier_60m",
            "modifier_80m",
            "modifier_100m",
            "modifier_150m",
            "modifier_200m",
            "modifier_250m",
            "modifier_300m",
            "modifier_400m",
            "modifier_600m",
            "modifier_1000m",
            "modifier_1500m",
        ],
    )

    ammo_df = pd.DataFrame(
        ammo_data,
        columns=[
            "id_code",
            "ammo_symbol",
            "name",
            "price",
            "availability",
            "crafting_difficulty",
            "description",
            "effect",
            "image",
            "weight",
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
        Column("weapon_class", String, ForeignKey("Weapon.id_code"), unique=True),
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
        Column("id_code", String(length=25), primary_key=True, unique=True),
        Column("name", String(length=25)),
        Column("description", String(length=400)),
        Column("modifier_10m", Integer),
        Column("modifier_20m", Integer),
        Column("modifier_30m", Integer),
        Column("modifier_40m", Integer),
        Column("modifier_60m", Integer),
        Column("modifier_80m", Integer),
        Column("modifier_100m", Integer),
        Column("modifier_150m", Integer),
        Column("modifier_200m", Integer),
        Column("modifier_250m", Integer),
        Column("modifier_300m", Integer),
        Column("modifier_400m", Integer),
        Column("modifier_600m", Integer),
        Column("modifier_1000m", Integer),
        Column("modifier_1500m", Integer),
    )

    ammo = Table(
        "Ammo",
        meta,
        Column("id_code", Integer, primary_key=True, autoincrement=True),
        Column("ammo_symbol", String(length=25), unique=True),
        Column("name", String(length=50)),
        Column("price", Integer),
        Column("availability", Integer),
        Column("crafting_difficulty", String(length=25)),
        Column("description", String(length=400)),
        Column("effect", String(length=50)),
        Column("image", String(length=50)),
        Column("weight", Integer),
    )

    meta.create_all(engine)

    # Inserting values from CSV into Table:
    ranged_df.to_sql("Ranged", con=connection, schema=None, if_exists="replace", index=False)
    weapon_df.to_sql("Weapon", con=connection, schema=None, if_exists="replace", index=False)
    ammo_df.to_sql("Ammo", con=connection, schema=None, if_exists="replace", index=False)
