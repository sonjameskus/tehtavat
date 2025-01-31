import math

def pizza(hinta, halkaisija):

    pizza1_hinta = float(input("Syötä ensimmäisen pizzan hinta: "))
    pizza1_halkaisija = float(input("Syötä ensimmäisen pizzan halkaisija senttimetreinä: "))
    pizza2_hinta = float(input("Syötä toisen pizzan hinta: "))
    pizza2_halkaisija = float(input("Syötä toisen pizzan halkaisija senttimetreinä: "))

    pizza1sade = pizza1_halkaisija / 2
    pizza1cm = pizza1sade ** 2 * math.pi
    pizza1m = pizza1cm / 10000
    pizza2sade = pizza2_halkaisija / 2
    pizza2cm = pizza2sade ** 2 * math.pi
    pizza2m = pizza2cm / 10000

    hinta1 = pizza1_hinta / pizza1m
    hinta2 = pizza2_hinta / pizza2m

    print(f"Ensimmäisen pizzan yksikköhinta on {hinta1:.2f} euroa / m2")
    print(f"Toisen pizzan yksikköhinta on {hinta2:.2f} euroa / m2")

    if hinta1 > hinta2:
        print("Toinen pizza antaa parempaa vastinetta rahalle.")
    elif hinta1 < hinta2:
        print("Ensimmäinen pizza antaa parempaa vastinetta rahalle.")
    else:
        print("Pizzat antavat yhtä hyvää vastinetta rahalle.")

pizza(1, 1)