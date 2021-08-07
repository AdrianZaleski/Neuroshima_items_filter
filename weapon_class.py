"""
Program do losowania broni dostępnej w ofercie u sprzedawcy z pliku CSV.
"""

import csv
from Neuroshima.modul_wypisanie_ogolne import wypisanie_ogolne

# Utworzenie zmiennych
nazwy_kolumn = []
weapon_wiersze = []

with open("CSV\\Bronie prototyp - WEAPON.csv", "r", encoding="utf-8") as weapon_CSV_raw:
    weapon_csv = csv.reader(weapon_CSV_raw, delimiter=",")

    nazwy_kolumn = next(weapon_csv)

    weapon_wiersze = [wiersz for wiersz in weapon_csv]
    weapon_CSV_raw.close()


# - Zmienna wykorzystywana w innych plikach. Możliwe bez 0 indeksu!
weapon_whole = weapon_wiersze.copy()
weapon_whole.insert(0, nazwy_kolumn)


if __name__ == '__main__':

    print(f"\nDostępne jest ogólnie: {len(weapon_wiersze)} pozycji amunicji do wyboru \n")  # Ilość pozycji broni przed sortowaniem

    wypisanie_ogolne(weapon_whole)

