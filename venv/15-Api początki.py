import requests
import json
import pprint

params = {

        "site" : "stackoverflow",
        "sort" : "votes",
        "fromdate" : "2022-08-01",
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
    pprint.pprint(questions)


