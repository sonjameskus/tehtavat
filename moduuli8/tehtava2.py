import mysql.connector


def lentoasemat(maakoodi):
    sql = (f"SELECT type, count(*) FROM airport WHERE iso_country='{maakoodi}' group by type")
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Maakoodilla {maakoodi} löytyy {rivi[1]} {rivi[0]} lentokenttätyyppiä.")
    return


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='sonja',
    password='Kirionkissa',
    autocommit=True,
    collation='utf8mb4_unicode_ci'
    )

maakoodi = input("Anna maakoodi: ")
lentoasemat(maakoodi)