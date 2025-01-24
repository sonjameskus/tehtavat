yritys = 5
while yritys > 0:
    yritys -= 1
    tunnus = input("Syötä käyttäjätunnus: ")
    salis = input("Syötä salasana: ")
    if tunnus == "python" and salis == "rules":
        print("Tervetuloa.")
        break
    if yritys == 0:
        print("Pääsy evätty.")
