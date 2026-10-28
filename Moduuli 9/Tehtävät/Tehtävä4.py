
import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


autot = []

for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

kilpailu_kaynnissa = True

while kilpailu_kaynnissa:

    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(nopeuden_muutos)
        auto.kulje(1)

        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynnissa = False


print(f"{'Rek.tunnus':<12}{'Huippunopeus':<15}{'Nopeus':<10}{'Matka':<12}")
print("-" * 49)

for auto in autot:
    print(
        f"{auto.rekisteritunnus:<12}"
        f"{auto.huippunopeus:<15}"
        f"{auto.nopeus:<10}"
        f"{auto.kuljettu_matka:<12.1f}"
    )