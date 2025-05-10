from flask import Flask, Response
import json

app = Flask(__name__)
@app.route('/alkuluku/<luku>/')
def alkuluku(luku):
    try:
        num = int(luku)
        if num <= 1:
            alkuluku = False
        else:
            alkuluku = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    alkuluku = False
                    break


        tilakoodi = 200
        vastaus = {
           "status" : tilakoodi,
           "luku" : num,
           "isPrime" : alkuluku
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status" : tilakoodi,
            "kuvaus" : "Virheellinen syöte"
        }

    json_vastaus = json.dumps(vastaus)
    return Response(response=json_vastaus, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "kuvaus" : "Virheellinen päätepiste"
    }
    json_vastaus = json.dumps(vastaus)
    return Response(response=json_vastaus, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
