import sqlite3

yhteys = sqlite3.connect("airports.sqlite")
kursori = yhteys.cursor()

maakoodi = input("Anna maakoodi (esim. FI): ")

sql = """
SELECT type, COUNT(*)
FROM airport
WHERE iso_country = ?
GROUP BY type
"""

kursori.execute(sql, (maakoodi.upper(),))
tulokset = kursori.fetchall()

for tyyppi, maara in tulokset:
    print(tyyppi, maara)

yhteys.close()