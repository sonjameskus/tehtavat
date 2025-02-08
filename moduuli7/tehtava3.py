lentoasemat= {}

while True:

    print("Kirjoita 'uusi', mikäli haluat syöttää uuden lentoaseman,"
          " 'haku', jos haluat hakea jo syötetyn lentoaseman tiedot"
          " tai 'lopeta' lopettaaksesi ohjelman.")
    kysymys = input("Syötä uusi, haku tai lopeta: ")

    if kysymys == "uusi":
        icao = input("Syötä lentoaseman ICAO-koodi: ")
        nimi = input("Syötä lentoaseman nimi: ")
        lentoasemat[icao] = nimi

    elif kysymys == "haku":
        icao = input("Syötä lentoaseman ICAO-koodi: ")

        if icao in lentoasemat:
            print(f"ICAO-koodilla {icao} löytyy lentoasema nimeltä {lentoasemat[icao]}")
        else:
            print("Lentoasemaa ei löytynyt.")

    if kysymys == "lopeta":
        break
