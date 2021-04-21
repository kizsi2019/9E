szam = int(input("Adj meg egy számot! "))
if szam % 3 == 0:
    print("osztható hárommal")
    if szam % 4 == 0:
    print("osztható néggyel")
if szam % 3 == 0 and szam % 24 == 0:
    print("osztható hárommal és néggyel")
if szam % 3 != 0 and szam % 24 != 0:
    print("nem osztható hárommal és néggyel sem")