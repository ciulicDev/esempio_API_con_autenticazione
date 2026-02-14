import csv 
import json
import requests

#config
input_file ="utenti_da_inviare.csv"
api_url = "https://api.example.com/users"  # esempio API reale
api_key = "LA_TUA_API_KEY"  # sostituisci con la tua chiave

#header con autenticazione

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

utenti = []


#lettura csv 

with open(input_file, newline="") as f:
    lettore = csv.DictReader(f)
    for riga in lettore:
        utenti.append({
            "name":riga["name"],
            "username":riga["username"],
            "email": riga["email"]
        })

risposte = []

#invio post con headers di autenticazione 

for u in utenti:
    response = requests.post(api_url, json=u, headers=headers)
    if response.status_code in [200,201]:
        risposte.append(response.json())
        print(f"{u["name"]} salvato con successo")
    elif response.status_code == 401:
        print(f"Errore di autenticazione per {u["name"]} (401)")
        risposte.append({
            "name":u["name"],
            "error": "Unauthorized"
        })
    
    else:
        print(f"Errore per {u["name"]}: {response.status_code}")
        risposte.append({
            "name": u["name"],
            "Error": response.status_code
        })