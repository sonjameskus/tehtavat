class Julkaisu:

    def __init__(self, nimi):
       self.nimi = nimi

class Kirja(Julkaisu):

    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Julkaisun nimi: {self.nimi} \nKirjoittaja: {self.kirjoittaja} \nSivumäärä: {self.sivumaara}")

class Lehti(Julkaisu):

    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Julkaisun nimi: {self.nimi} \nPäätoimittaja: {self.paatoimittaja}")


lehti = Lehti("Aku Ankka", "Aki Hyyppä")
kirja = Kirja("Hytti n:o 6", "Rosa Liksom", "200 sivua")

lehti.tulosta_tiedot()
kirja.tulosta_tiedot()

