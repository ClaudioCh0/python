kayttajatunnus = "python"
salasana = "rules"

yritykset = 0

while yritykset < 5:
    tunnus = input("Anna käyttäjätunnus: ")
    oikea_salasana = input("Anna salasana: ")

    if tunnus == kayttajatunnus and oikea_salasana == salasana:
        print("Tervetuloa")
        break
    else:
        yritykset += 1
        print("Väärä käyttäjätunnus tai salasana")

if yritykset == 5:
    print("Pääsy evätty")