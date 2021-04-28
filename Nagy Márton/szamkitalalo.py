import random
gondolt_szam = random.randint(1,5)
szam = int(input("Adj meg egy számot 1 - 5 között! "))
if szam == gondolt_szam:
    print("Eltaláltad! ")
elif szam < gondolt_szam:
    print("Ez kissebb mint a gondolt szám!")
else:
    print("Ez nagyobb mint a gondolt szám!")