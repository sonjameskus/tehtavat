def laske_summa(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa

luvut = [3, 6, 7, 8, 9]

print("Summa on " + str(laske_summa(luvut)))