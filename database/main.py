"""
Making a database from CSV file - take 1
- Using pandas for import data from CSV files with updated headers into main_database.db file

"""
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, ForeignKey
from mysql.connector import connect, Error


if __name__ == "__main__":
    difficulty_data = pd.read_csv(r"C:\\Python_Kurs\\Neuroshima\\CSV\\Bronie prototyp - DIFFICULTY.csv", header=0)
    difficulty_df = pd.DataFrame(difficulty_data)

    ammo_data = pd.read_csv(r"C:\\Python_Kurs\\Neuroshima\\CSV\\Bronie prototyp - AMMO.csv", header=0, skiprows=0)
    ammo_df = pd.DataFrame(ammo_data)

    ranged_data = pd.read_csv(r"D:\Python_Kurs\Neuroshima\CSV\Bronie prototyp - RANGED.csv", header=0)
    ranged_df = pd.DataFrame(ranged_data)

    weapon_data = pd.read_csv(r"D:\\Python_Kurs\\Neuroshima\\CSV\\Bronie prototyp - WEAPON.csv", header=0)
    weapon_df = pd.DataFrame(weapon_data)

    # Database segment:
    engine = create_engine(
        "sqlite:///C:\\Python_Kurs\\Neuroshima\\database\\main_database.db", echo=True
    )

    meta = MetaData()
    connection = engine.connect()

    meta.create_all(engine)

    # Inserting values from CSV into Table:
    ranged_df.to_sql("ranged", con=connection, schema=None, if_exists="replace", index=False)
    weapon_df.to_sql("weapons", con=connection, schema=None, if_exists="replace", index=False)
    ammo_df.to_sql("ammo", con=connection, schema=None, if_exists="replace", index=False)
    difficulty_df.to_sql("difficulty", con=connection, schema=None, if_exists="replace", index=False)

