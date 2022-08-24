# """
# json.dumps(data) - zapisuje dane do postaci Stringowej json
# json.dumb(data, nameOfFileHandler, ensure_ascii=False) - zapisuje dane do pliku w postaci json

# dump z ang. zsypać/zwalić/zrzucić
# """

# film = {
#     "title" : "Ale ja nie będę tego robił!",
#     "relase_year" : 1969,
#     "won_oscar" : True,
#     "actors" : ("Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"),
#     "budget" : None,
#     "credits" : {
#         "director" : "Arkadiusz Włodarczyk",
#         "writer" : "Alan Berger",
#         "animator" : "Anime Animatrix"
#         }
# }

# Json zamienia kod Python ten u góry (film) na kod json ten poniżej


# """
# {
#   "title":"Ale ja nie będę tego robił!",
#   "relase_year":1969,
#   "won_oscar":true,
#   "actors":[
#       "Arkadiusz Włodarczyk",
#       "Wiolleta Włodarczyk"
#   ]
#   "budget":null,
#   "credits":{
#       "directors":"Akadiusz Włodarczyk",
#       "writer":"Alan Berger",
#       "animator":"Anime Animatrix"
# """

# Wysyłanie danych w postaci string do pliku:
# import json

# encodingFilm = json.dumps(film, ensure_ascii=False)

# with open("sample.json", "w", encoding="UTF-8") as file:
#     json.dump(film,file,ensure_ascii=False)
#  #-----------------------------------------------------------------------

# odczytywanie pliku json na język python
# """
# json.loads(jsonstring) - przetwarza jsonString na dane python
# json.load(filePointer) - wczytuje json pliku i zwraca jako wynik metody dane typu python

# load z ang. - wczytać
# """

# import json

# encodedRetrievedMovie = '{"title": "Ale ja nie będę tego robił!", "relase_year": 1969, "won_oscar": true, "actors": ["Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"], "budget": null, "credits": {"director": "Arkadiusz Włodarczyk", "writer": "Alan Berger", "animator": "Anime Animatrix"}}'

# decodedMovie = json.loads(encodedRetrievedMovie)

# with open("sample.json", encoding="UTF-8") as file:
#     wynik = json.load(file)


# print(decodedMovie)
# print("\n")
# print(wynik)

#  #----------------------------------------------------------------------------------------
# """Dodając do json.dumbs w nawiasie komendę ident=4 robimy wcięcia w pliku i ładniej wygląda"""

# import json

# film = {
#     "title" : "Ale ja nie będę tego robił!",
#     "relase_year" : 1969,
#     "won_oscar" : True,
#     "actors" : ("Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"),
#     "budget" : None,
#     "credits" : {
#         "director" : "Arkadiusz Włodarczyk",
#         "writer" : "Alan Berger",
#         "animator" : "Anime Animatrix"
#         }
# }

# encodingFilm = json.dumps(film, ensure_ascii=False, indent=4)
# print(encodingFilm)

#  #-----------------------------------------------------------------------