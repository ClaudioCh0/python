import math


def yksikkohinta(halkaisija, hinta):
    sade = (halkaisija / 100) / 2
    pinta_ala = math.pi * sade ** 2
    yksikkohinta = hinta / pinta_ala

    return yksikkohinta

halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta (€): "))

halkaisija2 = float(input("Anna toisen pizzan halkaisija (cm): "))
hinta2 = float(input("Anna toisen pizzan hinta (€): "))

hinta_per_m2_1 = yksikkohinta(halkaisija1, hinta1)
hinta_per_m2_2 = yksikkohinta(halkaisija2, hinta2)

print(f"Ensimmäisen pizzan yksikköhinta: {hinta_per_m2_1:.2f} €/m²")
print(f"Toisen pizzan yksikköhinta: {hinta_per_m2_2:.2f} €/m²")

if hinta_per_m2_1 < hinta_per_m2_2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif hinta_per_m2_2 < hinta_per_m2_1:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Molemmat pizzat ovat yhtä edullisia.")