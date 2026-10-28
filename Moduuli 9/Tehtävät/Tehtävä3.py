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


auto = Auto("ABC-123", 142)

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)

print(f"Auton nopeus: {auto.nopeus} km/h")

auto.kulje(1.5)
print(f"Kuljettu matka: {auto.kuljettu_matka} km")

auto.kiihdyta(-200)
print(f"Auton nopeus hätäjarrutuksen jälkeen: {auto.nopeus} km/h")