import requests

def hae_vitsi():
    url = "https://api.chucknorris.io/jokes/random"

    vastaus = requests.get(url)

    if vastaus.status_code==200:
        vitsi_vastaus = vastaus.json()
        vitsi = vitsi_vastaus['value']
        print(vitsi)

    else:
        print("Tapahtui virhe.")

hae_vitsi()