import random

N = 0
n = 0

arvontojen_lkm = float(input("Syötä arvottavien pisteiden määrä: "))

while N < arvontojen_lkm:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if x**2 + y**2 < 1:
       n += 1
    N += 1

piin_likiarvo = 4*n/N
print(f'Piin likiarvo on {piin_likiarvo}')