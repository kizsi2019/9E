import random

gyujto = 0
i = 0
while i < 20:
    ertek = random.randint(1,12)
    if ertek % 3 == 0:
        print(ertek)
        gyujto = gyujto + 1 
    i = i + 1
print(gyujto, "db 3-al osztható szám volt")