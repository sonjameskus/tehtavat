kanta = input("Anna suorakulmion kanta: ")
korkeus = input("Anna suorakulmion korkeus: ")

kanta = float(kanta)
korkeus = float(korkeus)

piiri = kanta + kanta + korkeus + korkeus
ala = kanta * korkeus

print("Suorakulmion piiri: " + str(piiri))
print("Suorakulmion pinta-ala: " + str(ala))