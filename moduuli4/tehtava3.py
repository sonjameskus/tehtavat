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

if luvut:
    print("Pienin luku: " +  str(min(luvut)) + " ja suurin luku: " + str(max(luvut)))