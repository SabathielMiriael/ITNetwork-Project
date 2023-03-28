#  -------------------- Import pojištěnců ----------------------------------------
import Pojistenci

class Sprava:
    Pojistenci = None

    def __init__(self):
        self.Pojistenci = Pojistenci.Pojistenci()
#  -------------------- Spuštění správy pojištění ----------------------------------------
    def spustit(self):
        spusteno = True
        menu = """----------------------------------- 
Evidence pojištěných 
-----------------------------------\n
Vyberte si akci:
| 1 | - Přidat nového pojištěného
| 2 | - Vypsat všechny pojištěné
| 3 | - Vyhledat pojištěného
| 4 | - Smazat pojištěného
| 5 | - Konec\n"""
        while spusteno:
            print(menu)
            odpoved = input()
            spusteno = self.__akce(odpoved)
#  -------------------- Zadefinování akcí v menu --------------------
    def __akce(self, odpoved):
#  -------------------- Přidání nového pojišťeného
        if odpoved == "1":
            self.__pridat_do_seznamu()
            input("\nZáznam byl vložen.. Pokračujte klávesou ENTER...")
            return True
#  -------------------- Výpis pojišťených
        if odpoved == "2":
            self.Pojistenci.vypsat()
            input("\nPokračujte Pokračujte klávesou ENTER...")
            return True
#  -------------------- Vyhledání pojišťeného
        if odpoved == "3":
            self.__vyhledavani()
            input("\nPokračujte Pokračujte klávesou ENTER...")
            return True
#  -------------------- Smazání pojišťeného
        if odpoved == "4":
            self.__smazat_ze_seznamu()
            input("\nPokračujte Pokračujte klávesou ENTER...")
            return True
#  -------------------- Ukončení "programu" 
        if odpoved == "5":
            print("\nDěkuji za použití aplikace a přeji příjemný den, nashledanou.\n")
            return False
#  -------------------- Hláška v případě že zadám špatné číslo akce
        else:
            input("\nŠpatné zadání, prosím zvolte akci v rozmezí 1-5.\nPokračujte Pokračujte klávesou ENTER...")
            return True


#  -------------------- Akce: Přidání nového pojišťeného ----------------------------------------
    def __pridat_do_seznamu(self):
        jmeno, prijmeni, vek, telefon = self.__vlozeni_pojistence()
        self.Pojistenci.pridat(jmeno, prijmeni, vek, telefon)
#  -------------------- Akce: zapsání dat nového pojišťeného
    def __vlozeni_pojistence(self):
        jmeno = input("Prosím vložte jméno pojištěného:\n")
        prijmeni = input("Prosím vložte příjmení pojištěného:\n")
        vek = input("Prosím vložte věk pojištěného:\n")
        telefon = input("Prosím vložte telefonní číslo pojištěného:\n")
        return (jmeno, prijmeni, vek, telefon)
#  -------------------- Akce: Vyhledání pojišťeného
    def __vyhledavani(self):
        hotovo = False
        jmeno = ""
        prijmeni = ""
        telefon = ""
        vek = ""
#  -------------------- podle jakých dat má být pojistený vyhledán
        while not hotovo:
            print("""Jaké informace chcete vyhledat?
                | 1 | - Jméno
                | 2 | - Příjmení
                | 3 | - Věk
                | 4 | - Telefon?\n""")
            odpoved = input()
            if odpoved == "1":
                jmeno = input("Hledané Jméno? : ")
            else:
                if odpoved == "2":
                    prijmeni = input("Hledané Příjmení? : ")
                else:
                    if odpoved == "3":
                            vek = input("Hledaný Věk? : ")
                    else:
                        if odpoved == "4":
                            telefon = input("Hledané Telefonní číslo? : ")
                        else:
                            print("Prosím zadejte správné údaje")
            hotovo = input("Chcete zadat nějaké informace pro vyhledání? (y/n)\n") == "n"
        self.Pojistenci.vyhledat(jmeno, prijmeni, vek, telefon)
#  -------------------- Akce: Smazání pojišťeného
    def __smazat_ze_seznamu(self):
        jmeno, prijmeni, vek, telefon = self.__vlozeni_pojistence()
        if self.Pojistenci.smazat(jmeno, prijmeni, vek, telefon):
            print("Záznam smazán!")
        else:
            print("Záznam nenalazen, prosím zadejte data znovu.")
