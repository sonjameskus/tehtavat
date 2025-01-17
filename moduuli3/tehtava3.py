skp = input("Syötä biologinen sukupuoli (nainen/mies): ")
if skp == "nainen":
    hg = float(input("Syötä hemoglobiiniarvo (g/l): "))
    if (skp == "nainen" and hg < 117):
             print("Hemoglobiiniarvosi on alhainen.")
    if (skp == "nainen" and hg >= 117 and hg <= 175):
              print("Hemoglobiiniarvosi on normaali.")
    if (skp == "nainen" and hg > 175):
              print("Hemoglobiiniarvosi on korkea.")

if skp == "mies":
    hg2 = float(input("Syötä hemoglobiiniarvo (g/l): "))
    if (skp == "mies" and hg2<134):
         print("Hemoglobiiniarvosi on alhainen.")
    if (skp == "mies" and hg2>=134 and hg2<=195):
         print("Hemoglobiiniarvosi on normaali.")
    if (skp == "mies" and hg2>195):
         print("Hemoglobiiniarvosi on korkea.")