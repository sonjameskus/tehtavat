def bensiini(gallonat):
    return gallonat
while True:
    try:
       gallonat = float(input("Syötä gallonien määrä: "))
       litrat = gallonat * 3.785
       tulos = bensiini(litrat)
       print(f"{gallonat} gallonaa on {tulos:.3f} litraa.")
    except ValueError:
        print("Ohjelma lopetettu.")
        break