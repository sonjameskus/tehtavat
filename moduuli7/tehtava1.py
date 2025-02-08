vuodenajat = ("talvi", "kevät", "kesä", "syksy")
kuukausi = input("Syötä kuukauden numero: ")
talvi = (vuodenajat[0])
kevat = (vuodenajat[1])
kesa = (vuodenajat[2])
syksy = (vuodenajat[3])

if kuukausi == "1" or kuukausi == "2" or kuukausi == "12":
    print(f"{kuukausi}. kuukausi on {talvi}.")
elif kuukausi == "3"  or kuukausi == "4" or kuukausi == "5":
    print(f"{kuukausi}. kuukausi on {kevat}.")
elif kuukausi == "6" or kuukausi == "7" or kuukausi == "8":
    print(f"{kuukausi}. kuukausi on {kesa}.")
elif kuukausi == "9" or kuukausi == "10" or kuukausi == "11":
    print(f"{kuukausi}. kuukausi on {syksy}.")
else:
    print(f"{kuukausi}. kuukautta ei ole. Vuodenaikaa ei voi määrittää.")

