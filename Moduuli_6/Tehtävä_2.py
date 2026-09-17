import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

maksimi = int(input("Anna nopan tahkojen määrä: "))

while True:
    luku = heita_noppaa(maksimi)
    print(luku)

    if luku == maksimi:
        break