"""
Program do losowego filtrowania dostępnej amunicji u sprzedawcy z pliku CSV. Schemat działania:.
1. Import z pliku ammo_CSV
2. Używając funkcji randint sprawdzamy
    czy dostępność artykułu jest większa niż wylosowana wartość (0-100).
3. wyświetlanie wyników według zasady:
    l.p - nazwa kalibru - cena w walucie gry
"""

import csv
from random import randint as szansa



# Utworzenie zmiennych
from modul_wypisanie_nazwa_cena import wypisanie_nazwa_cena

nazwy_kolumn = []
ammo_wiersze = []

with open("CSV\\Bronie prototyp - AMMO.csv", "r", encoding="utf-8") as ammo_CSV_raw:
    ammo_csv = csv.reader(ammo_CSV_raw, delimiter = ",")

    nazwy_kolumn = next(ammo_csv)
    ammo_wiersze = list(ammo_csv)
    ammo_CSV_raw.close()


# - Zmienna wykorzystywana w innych plikach. Możliwe bez 0 indeksu!
ammo_whole = ammo_wiersze.copy()
ammo_whole.insert(0, nazwy_kolumn)


if __name__ == '__main__':
    # informacyjnie ilość pozycji amunicji przed sortowaniem
    print(f"\nDostępne jest ogólnie: {len(ammo_wiersze)} pozycji amunicji do wyboru \n")

    dostepne = []
    for kaliber in ammo_wiersze:
        opcja = szansa(0, 100)
        if int(kaliber[4]) >= opcja:
            dostepne.append(kaliber)

    # Dodanie zerwego wiersza z nazwami kolumn:
    dostepne.insert(0, nazwy_kolumn)

    # Wypisanie listy dostępnej u sprzedawcy jako i - nazwa, cena gambli:
    print(f"Po losowaniu dostępne jest: {len(dostepne)} pozycji.\n")
    wypisanie_nazwa_cena(dostepne, 2, 3)
