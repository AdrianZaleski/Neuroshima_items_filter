"""
Program for randomly filtering available ammunition the seller has from a CSV file. Working scheme:.
1. Import data from ammo_CSV
2. Using the randint function we check
    whether the availability of the article is greater than the randomly selected value (range 0-100).
3. displaying the results in order:
    l.p - caliber name (nazwa kalibru) - price in game currency (cena w walucie gry)
4. Additional menu for making new filtering form base CSV data.
"""

import csv
from random import randint as szansa

# Utworzenie zmiennych
from modul_wypisanie_nazwa_cena import wypisanie_nazwa_cena

nazwy_kolumn = []
ammo_wiersze = []

with open("CSV\\Bronie prototyp - AMMO.csv", "r", encoding="utf-8") as ammo_CSV_raw:
    ammo_csv = csv.reader(ammo_CSV_raw, delimiter=",")

    nazwy_kolumn = next(ammo_csv)
    ammo_wiersze = list(ammo_csv)
    ammo_CSV_raw.close()


# - Zmienna wykorzystywana w innych plikach. Możliwe bez 0 indeksu!
ammo_whole = ammo_wiersze.copy()
ammo_whole.insert(0, nazwy_kolumn)


if __name__ == '__main__':
    # informacyjnie ilość pozycji amunicji przed sortowaniem
    print(f"\nDostępne jest ogólnie: {len(ammo_wiersze)} pozycji amunicji do wyboru \n")

    available_ammo = []
    def available_ammo_func():

        for kaliber in ammo_wiersze:
            opcja = szansa(0, 100)
            if int(kaliber[4]) >= opcja:
                available_ammo.append(kaliber)

        # Dodanie zerwego wiersza z nazwami kolumn:
        available_ammo.insert(0, nazwy_kolumn)

        # # Wypisanie listy dostępnej u sprzedawcy jako i - nazwa, cena gambli:
        # print(f"Po losowaniu dostępne jest: {len(available_ammo)} pozycji.\n")
        # wypisanie_nazwa_cena(available_ammo, 2, 3)

        return available_ammo

    actual_ammo = available_ammo_func()
    print(f"Po losowaniu dostępne jest: {len(available_ammo)} pozycji.\n")
    wypisanie_nazwa_cena(actual_ammo, 2, 3)

    while True:
        print("\n \n")
        CHOICE = input("Czy chcesz wygenerować nową listę dostępną na stanie? T/N: ")
        if CHOICE == 't' or CHOICE == 'T':
            actual_ammo.clear()
            actual_ammo = available_ammo_func()
            # Wypisanie listy dostępnej u sprzedawcy jako i - nazwa, cena gambli:
            print(f"Po losowaniu dostępne jest: {len(available_ammo)} pozycji.\n")
            wypisanie_nazwa_cena(actual_ammo, 2, 3)
        elif CHOICE == 'N' or CHOICE == 'n':
            print('Koniec generowania')
            print(f"Finalnie dostępnych jest {len(available_ammo)} przedmiotów: \n")
            wypisanie_nazwa_cena(actual_ammo, 2, 3)
            break

