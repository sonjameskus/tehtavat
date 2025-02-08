nimet = set()

while True:
    nimi = input("Syötä nimi tai paina Enter lopettaaksesi: ")

    if nimi == "":
       break
    if nimi in nimet:
       print("Aiemmin syötetty nimi.")
    else:
       nimet.add(nimi)
       print("Uusi nimi.")

print("Syötit seuraavat nimet: ")
for nimi in nimet:
    print(nimi)
