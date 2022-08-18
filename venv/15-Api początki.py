# #***łączenie się ze stroną i pobieranie z niej zadań w JSON***
#
# import requests
# import json
# import pprint
# import webbrowser
#
#
# params = {
#
#         "site" : "stackoverflow",
#         "sort" : "votes",
#         "fromdate" : "2022-08-09",
#         "order" : "desc",
#         "tagged" : "python",
#         "min" : 15
# }
#
#
# r = requests.get("https://api.stackexchange.com/2.3/questions", params)
#
# try:
#     questions = r.json()
# except json.decoder.JSONDecodeError:
#     print("Niepoprawny format")
# else:
#     for question in questions["items"]:
#         webbrowser.open(question["link"]) #Otwieranie stron z odpowiednimi zadaniami w nowych oknach przeglądarki
#
#
