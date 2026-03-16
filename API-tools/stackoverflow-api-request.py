import requests
import json
import pprint

"""
API - Application Programming Interface
Skrypt pobierający odpowiedzi ze stackoverflow
minimalnie 15 punktów
posegregowane malejąco
z ostatniego tygodnia
z kategorii Python
"""

params = {
    "site" : "stackoverflow",
    "sort" : "votes",
    "order" : "desc",
    "fromdate" : "2026-01-01",
    "tagged" : "python",
    "min" : 7
}

r= requests.get("https://api.stackexchange.com/2.3/questions/", params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny Format")
else:
    for question in questions["items"]:
        pprint.pprint(question["link"]) #Ładne prezentowanie z indentami
