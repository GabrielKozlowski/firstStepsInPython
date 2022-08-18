
import requests
import json
import webbrowser

from datetime import datetime, timedelta

dayBefore = timedelta(days=7)
dateSearch = datetime.today() - dayBefore


params = {

        "site" : "stackoverflow",
        "sort" : "votes",
        "fromdate" : int(dateSearch.timestamp()),
        "order" : "desc",
        "tagged" : "python",
        "min" : 15
}


r = requests.get("https://api.stackexchange.com/2.3/questions", params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for question in questions["items"]:
        webbrowser.open(question["link"])

