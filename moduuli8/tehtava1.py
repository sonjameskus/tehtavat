import mysql.connector


def icaokoodi(koodi):
    sql = f"SELECT ident, name, municipality FROM airport where ident='{koodi}'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"ICAO-koodi {rivi[0]} on lentoaseman {rivi[1]} koodi. Se sijaitsee kunnassa {rivi[2]}.")
    return

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='sonja',
    password='Kirionkissa',
    autocommit=True,
    collation='utf8mb4_unicode_ci'
)

koodi = input("Anna lentoaseman ICAO-koodi: ")
icaokoodi(koodi)
