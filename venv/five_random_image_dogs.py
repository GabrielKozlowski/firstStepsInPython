import requests
import json
import webbrowser

r = requests.get("https://dog.ceo/api/breeds/image/random/5")


try:
    photo = r.json()
except json.decoder.JSONDecodeError:
    print("Bad format")
else:
    for pictur in photo['message']:
        webbrowser.open(pictur)