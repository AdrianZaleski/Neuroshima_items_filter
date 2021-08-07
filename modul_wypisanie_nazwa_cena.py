"""
Moduł wypisujacy nazwe oraz cene
 TODO Scalic z innymi modulami wypisujacymi i zrobic jeden modul konfigurowalny
"""

# Wypisanie konkretnych pozycji z listy w liście po nazwie i cenie:
def wypisanie_nazwa_cena(lista, id_nazwa, id_ceny):
    for index, nazwa in enumerate(lista):
        print(f"{index} - {nazwa [id_nazwa]}, {nazwa [id_ceny]} gambli")
