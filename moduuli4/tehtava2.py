tuuma = int(input("Anna tuumat: "))
cm = tuuma * 2.54
while tuuma!=">0":
    if tuuma <0:
        break
    print(str(cm) + "cm")
    tuuma += 1
    tuuma = int(input("Anna tuumat: "))
    cm = tuuma * 2.54

