luvut = []

while True:
    luku_str = input("Anna luku tai lopeta painamalla Enter: ")
    if luku_str == "":
        break

    try:
        luku = float(luku_str)
        luvut.append(luku)
    except ValueError:
        print("Anna oikea luku. ")


luvut.sort(reverse=True)
print("Viisi suurinta numeroa ovat: ")
for i in range(5):
   print(luvut[i], end="   ")