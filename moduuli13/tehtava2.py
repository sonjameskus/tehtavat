from flask import Flask, Response
import json
import mysql.connector

app = Flask(__name__)

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='keltanokat',
    password='lentopeli',
    autocommit=True,
    collation='utf8mb3_general_ci'
)

@app.route("/kentta/<icao>")
def hae_tiedot(icao):
    try:
        sql = f"SELECT ident, name, municipality FROM airport where ident='{icao}'"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        rivi = kursori.fetchone()
        kursori.close()

        if rivi:
            vastaus = {
                "ICAO": rivi[0],
                "Name": rivi[1],
                "Municipality" : rivi[2]
            }
            tilakoodi = 200
        else:
            vastaus = {
                "status": 404,
                "kuvaus": "Lentokenttää ei löydy"
            }
            tilakoodi = 404

    except Exception as e:
        tilakoodi = 500
        vastaus = {
            "status": tilakoodi,
            "kuvaus": f"Palvelinvirhe: {str(e)}"
        }

    json_vastaus = json.dumps(vastaus)
    return Response(response=json_vastaus, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": 404,
        "kuvaus": "Virheellinen päätepiste"
    }
    json_vastaus = json.dumps(vastaus)
    return Response(response=json_vastaus, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)