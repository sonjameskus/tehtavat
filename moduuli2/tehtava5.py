leiviska = input("Anna leiviskät: ")
naula = input("Anna naulat: ")
luoti = input("Anna luodit: ")

leiviska = float(leiviska)
naula = float(naula)
luoti = float(luoti)

luoti_g = luoti*13.3
naula_g = naula*32*13.3
leiviska_g = leiviska*20*32*13.3

leiviska_g = float(leiviska_g)
naula_g = float(naula_g)
luoti_g = float(luoti_g)

gramma = leiviska_g + naula_g + luoti_g
kg = gramma//1000


print(f"Massa nykymittojen mukaan: {kg} kilogrammaa ja{gramma%1000:10.2f}grammaa")
