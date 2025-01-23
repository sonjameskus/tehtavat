import random
luku = random.randint(1, 10)

while True:
    arvaus = input("Arvaa lukua väliltä 1-10: ")
    try: arvaus = int(arvaus)
    except ValueError:
        print("Syötä oikea luku.")
        continue
    if arvaus < luku:
      print("Liian pieni arvaus.")
    elif arvaus > luku:
      print("Liian suuri arvaus.")
    elif luku == arvaus:
      print("Oikein!")
      break

