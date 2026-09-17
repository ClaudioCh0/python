import random

arvottu = random.randint(1, 10)
arvaus = int(input("Arvaa luku välillä 1...10 "))

while arvaus != arvottu:
    if arvaus > arvottu:
        print("Liian suuri arvaus")
    elif arvaus > arvottu:
        print("Liian pieni arvaus")
    arvaus = int(input("Arvaa uudelleen: "))

print("Oikein")