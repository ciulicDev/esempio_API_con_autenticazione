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