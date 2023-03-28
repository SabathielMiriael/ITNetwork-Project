#  -------------------- definice pojištěného ----------------------------------------
class Pojisteny:

    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon
#  -------------------- fromat jak bude pojisteny zobrazen
    def zobrazit(self):
        print(f"{self.jmeno} {self.prijmeni}\t{self.vek}\t{self.telefon}")

#  -------------------- Všeobecná práce s pojištěnci ----------------------------------------
class Pojistenci:
    __pojistenci = []
#  -------------------- Přidat pojištěnce
    def pridat(self, jmeno, prijmeni, vek, telefon):
        self.__pojistenci.append(Pojisteny(jmeno, prijmeni, vek, telefon))
#  -------------------- Vypsat pojištěné
    def vypsat(self):
        if len(self.__pojistenci) == 0:
            print("Žádná data nenalezena.")
        else:
            for pojisteny in self.__pojistenci:
                pojisteny.zobrazit()
#  -------------------- Vyhledsat pojištěnce, 
    def vyhledat(self, jmeno, prijmeni, vek, telefon):
        if len(self.__pojistenci) == 0:
            print("Žádná data nenalezena.")
        else:
            for pojisteny in self.__pojistenci:
                if jmeno in pojisteny.jmeno and prijmeni in pojisteny.prijmeni and vek in pojisteny.vek and telefon in pojisteny.telefon:
                    pojisteny.zobrazit()
#  -------------------- Smazat pojištěnce, nutnost zapamatovat si koho chci smazat a jeho data
    def smazat(self, jmeno, prijmeni, vek, telefon):
        for pojisteny in self.__pojistenci:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni and pojisteny.vek == vek and pojisteny.telefon == telefon :
                self.__pojistenci.remove(pojisteny)
                return True
        return False
