"""
Script takes Restcountries Name of Country with respective Geographical position
"""
from socket import timeout

import requests
import json
import webbrowser

params = {
    timeout : 5
    }

r = requests.get("https://restcountries.com/v3.1/independent?status=true", params=params)

try:
    content = r.json()
    for country in content:
        print(country["name"]["common"])
        print(country["latlng"])
except json.decoder.JSONDecodeError:
    print("niepoprawny format")
