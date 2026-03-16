"""
Script checks Cat API health
"""

import requests
import json
import pprint
import webbrowser
from datetime import datetime, timedelta

url = "https://alexwohlbruck.github.io/cat-facts/docs/endpoints/facts.html"

r = requests.get(url, timeout=5)

print("status:", r.status_code)
print("headers", r.headers.get("content-type"))
print("text (first 300):", r.text[:300])
