import random

maara = int(input("Montako arpakuutiota heitetään: "))

summa = 0

for i in range(maara):
    luku = random.randint(1, 6)
    summa += luku

print(f"Silmälukujen summa: {summa}")
