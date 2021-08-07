"""
Moduł mający zebrane różne własne funkcje:
- Wypisanie wszystkich wierszy
- Wypisanie wierszy z konkretnym indexem
"""

# Wypisanie konkretnych pozycji z listy w liście po nazwie i cenie:
def wypisanie_nazwa_cena_typ(lista, id_nazwa, id_ceny, id_typ, id_ammo, id_avail):
    for index, nazwa in enumerate(lista):
        print(f"{index} - {nazwa[id_typ]} - {nazwa [id_nazwa]} - na: {nazwa[id_ammo]} - cena: {nazwa [id_ceny]} gambli - "
              f"dostępność: {nazwa[id_avail]}")


