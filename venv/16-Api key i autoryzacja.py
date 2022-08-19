import requests
import json
import credentials


r = requests.get("https://api.thecatapi.com/v1/favourites", headers=credentials.headers)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Bad format")
else:
    print(content)