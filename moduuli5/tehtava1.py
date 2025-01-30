import random

nopat = int(input("Anna arpakuutioiden lukumäärä: "))
lkm = []
for nopat in range(0, (nopat)):
    noppa = int(random.randint(1,6))
    lkm.append(noppa)
print(lkm)
print(sum(lkm))