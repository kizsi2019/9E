szam = int(input("Adj meg egy számot! "))
if szam > 0 and szam % 2 == 0:
    print("pozitív páros")
if szam < 0 and szam % 2 != 0:
    print("negatív páratlan")