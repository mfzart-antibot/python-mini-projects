"""
API - Application Programming Interface
    BLOK GOTOWEGO KODU DO OTWIERANIA ROZNYCH API
    BLOCK PREPARED FOR DESIRED API OPENING
"""

import requests
import json

r= requests.get("", timeout=5)

try:
    questicons = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny Format")
else:
    print("Error")