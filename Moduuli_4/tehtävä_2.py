tuuma = float(input("Montako tuumaa haluat muuntaa: "))

while tuuma >= 0:
    cm = tuuma * 2.54
    print(f"{tuuma} on {cm:.2f} senttimetriä")
    tuuma = float(input("Anna tuuma: "))
