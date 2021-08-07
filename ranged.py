"""
Losowanie broni wszelakiej:
# DONE: Próba wczytania pliku CSV z rodzajami broni.
# Poniższe założenia do spełnienia aby uzyskać minimalną funkcjonalność:
# DONE : Utworzenie list z pozycjami: rozdzielić nazwy od pozycji.
# DONE : Przerobienie pozycji "Availability" na cyfrę
# DONE : Wyliczenie przy użyciu random które pozycje będą dostępne
# DONE : Wypisanie wszystkich pozycji, dla których warunek został spełniony.
# DONE : Wypisanie pojedynczych nazw wylosowaych, rodzaju broni, nazwy, kalibru, ceny i dostępnośći
        - DONE: Dopisać aby kaliber był normalnie opisany a nie jako id_kaliber,
# TODO : Wybór rodzaju broni według indeksu - wypisanie według powyższej zależnośći
# TODO : Menu wyboru opcji:
        - Wyświetlenie filtrowania po gatunku broni
- DONE - Wyświetlenie filtrowania defaultowego

# DONE : Wyświetlenie filtrowania dodatkowo przedmiotów powyżej jakieś dostępności
TODO - dorobić możliwość ponownego shuffle wejściowych danych z CSV.




"""


import csv
from random import randint as szansa

from modul_wypisanie_nazwa_cena_typ import wypisanie_nazwa_cena_typ
from modul_wypisanie_ogolne import wypisanie_ogolne
from ammo import ammo_whole as amunicja
from weapon_class import weapon_whole as typ_broni



# Otwarcie odpowiedniego pliku CSV i przypisanie do niego wartości:
with open("CSV\\Bronie prototyp - RANGED.csv", "r", encoding="utf-8") as ranged_CSV_raw:
    ranged_CSV = csv.reader(ranged_CSV_raw, delimiter=",")

    nazwy_kolumn = next(ranged_CSV)

    ranged_wiersze = list(ranged_CSV)
    ranged_CSV_raw.close()


if __name__ == '__main__':

    # Wypisanie pozycji indeksów jakie są dostępne - TODO : Po wszystkim zakomentować tę opcję.
    print("Pozycje w kolumnach jakie są dostępne i ich indeksy:")
    wypisanie_ogolne(nazwy_kolumn)

    # Wyspisanie ile jest pozycji przed losowaniem dostępności:
    print(f"\nPrzed filtrowaniem jest dostępne: {len(ranged_wiersze)} pozycji broni.\n")


    #  Tabela z dostępnymi broniami po filtrowaniu (według Availability)
    dostepne_bronie_random = []
    for gun in ranged_wiersze:
        opcja = szansa(0, 100)
        if int(gun[16]) >= opcja:
            dostepne_bronie_random.append(gun)

    # Dodanie zerwego wiersza z nazwami kolumn - przydatne do wypisywania tabeli co jest czym:
    dostepne_bronie_random.insert(0, nazwy_kolumn)


    MENU = " "
    while True:
        print("\nWitaj w mej zrbojowni!")
        print("1 - prosty odsiew listy\n"
              "2 - przedmioty powyzej pewnej dostępności\n"
              "3 - Przedmioty rzadkie\n"
              "4 - Konkretny gatunek broni\n"
              "0 - exit")

        MENU = int(input("Wybierz opcje: "))

        # Koniec programu
        if MENU == 0:
            print("Adios!")
            break

        # Wyświetlanie pozycji filtrowanej w fomrmacie: lp. Class, Name, Kaliber, Price
        # Dodatkowo zapis wartości do pliku csv
        if MENU == 1:
            print(f"\nAktualnie dostępny stock zawiera {len(dostepne_bronie_random) -1} pozycji:\n")

            for nazwa in dostepne_bronie_random:
                for kaliber in amunicja:
                    if nazwa[3] == kaliber[0]:
                        nazwa[3] = kaliber[2]
            wypisanie_nazwa_cena_typ(dostepne_bronie_random, 1, 15, 2, 3, 16)
            with open('bronie_random.csv', 'w', newline='') as f:
                write = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=';')

                write.writerows(dostepne_bronie_random)
            print("\nZapisano wartości do pliku: bronie_random.csv\n")


        # Wyświetlanie pozycji filtrowanej zależnie od minimalnej dostępności w fomrmacie:
        # lp. Class, Name, Kaliber, Price
        if MENU == 2:
            poziom_sklepu = int(input("Podaj poziom dostępności towaru "
                                      "powyżej którego sprzedawca ma sprzęt (0-100): "))

            dostepne_bronie_od_avail = []
            for gun in ranged_wiersze:
                opcja = szansa(0, 100)
                if int(gun[16]) >= opcja and int(gun[16]) >= poziom_sklepu:
                    dostepne_bronie_od_avail.append(gun)
            wypisanie_nazwa_cena_typ(dostepne_bronie_od_avail, 1, 15, 2, 3, 16)

        # Wyświetlanie listy dla odpowiedniego typu broni (pistol, karabin tec.):
        if MENU == 3:
            weapon_class_pomocnicza = []
            for nazwa in ranged_wiersze:
                weapon_class_pomocnicza.append(nazwa[2])
            weapon_class = sorted(list(dict.fromkeys(weapon_class_pomocnicza)))

            for nazwa in weapon_class:
                for typ in typ_broni:
                    if nazwa == typ[0]:
                        nazwa = typ[1]

            wypisanie_ogolne(weapon_class)

            # sub_menu = " "
            # while sub_menu != 0:
            #     print("Dostępne opcje w menu:\n"
            #           "1 - Edycja listy wyboru typu broni\n"
            #           "2 - Wyświetlenie dostępnych broni według kryteriów.\n"
            #           "9 - Wyczyszczenie całkowite listy\n"
            #           "0 - Powrót")
            #     sub_menu = int(input("Wybierz opcje: "))
            #     if sub_menu == 1:
            #         weapon_choice = []
            #         print(f'Dostępne są poniższe kategorie broni: ')
            #         modul.wypisanie_ogolne(weapon_class)
            #         a = int(input('Proszę wybrać pozycję do późniejszego wyświetlenia: '))
            #         weapon_choice.append(weapon_class[int(a)])
            #         print(weapon_choice)
            #
            #     if sub_menu == 0:
            #          pass
