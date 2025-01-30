kaupungit = []

for _ in range(5):
    kaupunki = input("Syötä kaupungit: ")
    kaupungit.append(kaupunki)

for kaupunki in kaupungit:
    print(f"{kaupunki}")