class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylös(self):
        if self.kerros < self.ylin:
            self.kerros +=1
            print(f"Hissi on kerroksessa {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -=1
            print(f"Hissi on kerroksessa {self.kerros}")

    def siirry_kerrokseen(self, haluttu_kerros):
        while self.kerros < haluttu_kerros:
            self.kerros_ylös()
        while self.kerros > haluttu_kerros:
            self.kerros_alas()

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = []
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_lkm = hissien_lkm
        for i in range (hissien_lkm):
            hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(hissi)

    def aja_hissiä(self, hissin_numero, kohdekerros):
        hissi = self.hissit[hissin_numero]
        print(f"Tällä hetkellä liikkuu hissi numero {hissin_numero}")
        hissi.siirry_kerrokseen(kohdekerros)

    def palohälytys(self):
        print("Palohälytys! Kaikkien hissien mentävä alas!")
        for hissin_numero, hissi in enumerate(self.hissit):
            if hissi.kerros == hissi.alin:
                print(f"Hissi {hissin_numero} on valmiiksi alimmassa kerroksessa.")
            else:
                print(f"Hissi numero {hissin_numero} liikkuu:")
                hissi.siirry_kerrokseen(self.alin_kerros)

#tehtävä 1
h = Hissi(1, 10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)

#tehtävä 2

talo = Talo(1, 10, 6)
talo.aja_hissiä(3, 7)
talo.aja_hissiä(2, 4)
talo.aja_hissiä(5, 9)

#tehtävä 3

talo.palohälytys()