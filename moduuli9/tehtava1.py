import random
from texttable import Texttable

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus="0", matka="0"):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = int(nopeus)
        self.matka = int(matka)

    def kiihdyta(self, muutos):
        nopeus_nyt = self.nopeus + muutos
        if nopeus_nyt > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif nopeus_nyt < 0:
            self.nopeus = 0
        else:
            self.nopeus = nopeus_nyt

    def kulje(self, tunnit):
       self.matka += tunnit * self.nopeus


#1
auto = Auto("ABC-123", 142)
print (f"Auton rekisteritunnus on {auto.rekisteritunnus} ja huippunopeus on {auto.huippunopeus} km/h."
       f" Auton tämänhetkinen nopeus on {auto.nopeus} km/h ja kuljettu matka {auto.matka} km.")

#2
auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print(f"Auton nopeus: {auto.nopeus} km/h.")
auto.kiihdyta(-200)
print(f"Auton nopeus: {auto.nopeus} km/h.")

#3
auto.kiihdyta(60)
auto.kulje(1.5)
print(f"Auto on kulkenut {auto.matka} km 1,5 tunnin aikana.")

#4
autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

tunti = 0
while True:
    tunti += 1
    print(f"\n{tunti}. tunti")

    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdyta(muutos)

    for auto in autot:
        auto.kulje(1)
        print(
            f"{auto.rekisteritunnus} kulki {auto.nopeus} km/h ja {auto.matka} km.")

    kilpailun_loppu = False
    for auto in autot:
        if auto.matka >= 10000:
            kilpailun_loppu = True
            print(f"\nKilpailu loppui. {auto.rekisteritunnus} on ajanut 10 000 km.")
            break
    if kilpailun_loppu:
        break

autot_sorted = sorted(autot, key=lambda auto: auto.matka, reverse=True)
print("\nTulokset:\n")

t = Texttable()
t.add_row(['Rekisteritunnus', 'Huippunopeus (km/h)', 'Nopeus (km/h)', 'Matka (km)'])
for auto in autot_sorted:
   t.add_row([auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.matka])
print(t.draw())