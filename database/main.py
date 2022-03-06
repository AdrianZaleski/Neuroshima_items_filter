"""
Making a database from CSV file - take 1
- Using pandas for import data from CSV files with updated headers into main_database.db file

"""
import sqlite3

import pandas as pd
from mysql.connector import Error


database = r"C:\\Python_Kurs\\Neuroshima\\database\\main_db.db"


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_tables(database):
    sql_create_difficulty_table = """CREATE TABLE IF NOT EXISTS difficulty (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                range INTEGER NOT NULL,
                modifier INTEGER NOT NULL 
                ); """

    sql_create_damage_table = """CREATE TABLE IF NOT EXISTS damage (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT,
                    symbol TEXT UNIQUE,
                    effect_on_target TEXT, 	
                    flat_modifier INTEGER NOT NULL,	
                    pain_modifier INTEGER NOT NULL,	
                    head_description TEXT,
                    torso_description TEXT,
                    r_arm_description TEXT,
                    l_arm_description TEXT,
                    leg_description TEXT
                    ); """

    sql_create_ammo_table = """CREATE TABLE IF NOT EXISTS ammo (
                id_code TEXT PRIMARY KEY,
                ammo_symbol TEXT NOT NULL,
                name TEXT NOT NULL,
                price INTEGER NOT NULL,
                availability INTEGER,
                crafting_difficulty TEXT ,
                description TEXT,
                effect TEXT,
                image BLOB,
                weight INTEGER,
                FOREIGN KEY (crafting_difficulty) REFERENCES difficulty (id)
                ); """

    sql_create_weapon_table = """CREATE TABLE IF NOT EXISTS weapon (
                id_code TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                modifier_10m INTEGER,
                modifier_20m INTEGER,
                modifier_30m INTEGER,
                modifier_40m INTEGER,
                modifier_60m INTEGER,
                modifier_80m INTEGER,
                modifier_100m INTEGER,
                modifier_150m INTEGER,
                modifier_200m INTEGER,
                modifier_250m INTEGER,
                modifier_300m INTEGER,
                modifier_400m INTEGER,
                modifier_600m INTEGER,
                modifier_1000m INTEGER,
                modifier_1500m INTEGER
                ); """

    sql_create_ranged_table = """CREATE TABLE IF NOT EXISTS ranged (
                id_code TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                weapon_class TEXT NOT NULL,
                ammo TEXT NOT NULL,
                magazine INTEGER NOT NULL,
                misfire_roll INTEGER NOT NULL,
                celnosc_w_procentach INTEGER,
                zasięg_[m] INTEGER,
                fire_rate INTEGER,
                attack_type TEXT,
                reload INTEGER,
                punkty_przebicia INTEGER NOT NULL,
                damage TEXT,
                strength INTEGER, 
                holster INTEGER NOT NULL,
                price INTEGER NOT NULL,
                availability INTEGER NOT NULL,
                actions TEXT,
                description TEXT,
                image BLOB,
                
                FOREIGN KEY (weapon_class) REFERENCES weapon (id_code),
                FOREIGN KEY (ammo) REFERENCES ammo (id_code),
                FOREIGN KEY (damage) REFERENCES damage (symbol)
                ); """

    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create difficulty table
        create_table(conn, sql_create_difficulty_table)

        # create ammo table
        create_table(conn, sql_create_ammo_table)

        # create weapon table
        create_table(conn, sql_create_weapon_table)

        # create ranged table
        create_table(conn, sql_create_ranged_table)

        # create damage table
        create_table(conn, sql_create_damage_table)

    else:
        print("Error! cannot create the database connection.")


def csv_data_into_db_import(database):
    # Read data from files
    difficulty_data = pd.read_csv(
        r"C:\\Python_Kurs\\Neuroshima\\CSV\\Bronie prototyp - DIFFICULTY.csv",
        header=0, skiprows=0
    )
    difficulty_df = pd.DataFrame(difficulty_data)

    ammo_data = pd.read_csv(
        r"C:\\Python_Kurs\\Neuroshima\\CSV\\Bronie prototyp - AMMO.csv",
        header=0, skiprows=0
    )
    ammo_df = pd.DataFrame(ammo_data)

    ranged_data = pd.read_csv(
        r"C:\Python_Kurs\Neuroshima\CSV\Bronie prototyp - RANGED.csv",
        header=0, skiprows=0
    )
    ranged_df = pd.DataFrame(ranged_data)

    weapon_data = pd.read_csv(
        r"C:\\Python_Kurs\\Neuroshima\\CSV\\Bronie prototyp - WEAPON.csv",
        header=0, skiprows=0
    )
    weapon_df = pd.DataFrame(weapon_data)

    # Read data from files
    damage_data = pd.read_csv(
        r"C:\\Python_Kurs\\Neuroshima\\CSV\\Bronie prototyp - DAMAGE.csv",
        header=0, skiprows=0
    )
    damage_df = pd.DataFrame(damage_data)


    # Inserting values from CSV into Table:
    conn = create_connection(database)

    # rename the headers in DataFrame files:
    db_cols = list(pd.read_sql('SELECT * FROM ammo', conn))  # where ... is your table will return columns as list
    ammo_df = ammo_df.rename(columns=dict(zip(ammo_df.columns, db_cols)))

    db_cols = list(pd.read_sql('SELECT * FROM difficulty', conn))
    difficulty_df = difficulty_df.rename(columns=dict(zip(difficulty_df.columns, db_cols)))

    db_cols = list(pd.read_sql('SELECT * FROM ranged', conn))
    ranged_df = ranged_df.rename(columns=dict(zip(ranged_df.columns, db_cols)))

    db_cols = list(pd.read_sql('SELECT * FROM weapon', conn))
    weapon_df = weapon_df.rename(columns=dict(zip(weapon_df.columns, db_cols)))

    db_cols = list(pd.read_sql('SELECT * FROM damage', conn))
    damage_df = damage_df.rename(columns=dict(zip(damage_df.columns, db_cols)))



    difficulty_df.to_sql("difficulty", con=conn, schema=None, if_exists="append", index=False, index_label=None)
    ammo_df.to_sql("ammo", con=conn, schema=None, if_exists="append", index=False, index_label=None)
    weapon_df.to_sql("weapon", con=conn, schema=None, if_exists="append", index=False)
    ranged_df.to_sql("ranged", con=conn, schema=None, if_exists="append", index=False)
    damage_df.to_sql("damage", con=conn, schema=None, if_exists="append", index=False)

    return print('Importing values: Done')


if __name__ == "__main__":
    create_tables(database)

    csv_data_into_db_import(database)
