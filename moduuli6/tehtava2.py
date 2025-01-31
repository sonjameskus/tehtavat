import random

def noppa(tahkot):
       tulos = random.randint(1,tahkot)
       return tulos

tahkot = int(input("Syötä nopan maksimisilmäluku: "))

while True:
    tulos = noppa(tahkot)
    print(tulos)
    if tulos == tahkot:
        break
