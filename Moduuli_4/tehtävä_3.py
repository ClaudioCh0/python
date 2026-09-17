syote = input("Anna luku: ")

if syote == "":
    print("Et syöttänyt yhtään lukua.")
else:
    luku = int(syote)
    pienin = luku
    suurin = luku

    syote = input("Anna luku: ")

    while syote != "":
        luku = int(syote)

        if luku < pienin:
            pienin = luku

        if luku > suurin:
            suurin = luku

        syote = input("Anna luku: ")

    print("Pienin luku:", pienin)
    print("Suurin luku:", suurin)