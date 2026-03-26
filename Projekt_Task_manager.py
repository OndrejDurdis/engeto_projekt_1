# Správce úkolů

ukoly = []


def hlavni_menu():
    while True:
        print("1. Přidat nový úkol.")
        print("2. Zobrazit všechny úkoly.")
        print("3. Odstranit úkol.")
        print("4. Konec programu.")
        volba = input("Vyberte možnost (1-4): ").strip()

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu.")
            break
        else:
            print("Neplatná volba.")


def pridat_ukol():
    """Přídá nový úkol"""
    nazev = input("Zadejte název úkolu: ").strip()
    popis = input("Zadejte popis úkolu: ").strip()
    if nazev:
        novy_ukol = {"nazev": nazev, "popis": popis}
        ukoly.append(novy_ukol)
        print(f"Úkol '{nazev}' byl přidán.")
    else:
        print("Úkol musí mít název.")


def zobrazit_ukoly():
    """Zobrazí seznam úkolů"""
    if not ukoly:
        print("Žádné úkoly zatím nejsou.")
    else:
        print("Seznam úkolů:")
        for i, ukol in enumerate(ukoly, start = 1):
            print(f"{i}. {ukol['nazev']} - {ukol['popis']}")
        print()
    

def odstranit_ukol():
    """Odstraní úkol ze seznamu úkolů"""
    zobrazit_ukoly()
    if ukoly:
        try:
            cislo = int(input("Zadejte číslo úkolu k odstranění: "))
            if 1 <= cislo <= len(ukoly):
                smazany = ukoly.pop(cislo - 1)
                print(f"Úkol '{smazany['nazev']}' byl odstraněn.")
            else:
                print("Neplatné číslo úkolu.")
        except ValueError:
            print("Zadejte platné číslo úkolu.")


if __name__ == "__main__":
    hlavni_menu()