#*** Zadanie z importem 5 faktów o kotach albo psach pobranych ze stron***
# import requests
# import json
# from pprint import pprint
#
#
# message = '''
# Welcome in my program. You can chose one of two options.
#
# press 1 to print 5 facts of cats or
# press 2 to print 5 facts of dogs
# '''
#
#
#
#
#
# r = requests.get("https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=5")
# d = requests.get("http://dog-api.kinduff.com/api/facts?number=5")
#
#
#
# try:
#     catFacts = r.json()
#     dogFacts = d.json()
#
# except json.decoder.JSONDecodeError:
#     print('Bad format')
# else:
#     while True:
#         chose = input(message)
#         if chose == '1':
#             for cat in catFacts:
#                 pprint(cat['text'])
#             break
#         elif chose == '2':
#             pprint(dogFacts['facts'])
#             break
#         else:
#             print("You can only write 1 or 2")
#             continue
#
# ---------------------------------------------------------------------------------
#***Zadanie pobrania 5 losowych zdjęć psów i otwarcie ich w przeglądarce***
#
# import requests
# import json
# import webbrowser
#
# r = requests.get("https://dog.ceo/api/breeds/image/random/5")
#
#
# try:
#     photo = r.json()
# except json.decoder.JSONDecodeError:
#     print("Bad format")
# else:
#     for pictur in photo['message']:
#         webbrowser.open(pictur)
#
# ------------------------------------------------------------------------


import requests
import json

r = requests.get("https://meowfacts.herokuapp.com/?count=5")


try:
    photo = r.json()
except json.decoder.JSONDecodeError:
    print("Bad format")
else:
    print(photo)
