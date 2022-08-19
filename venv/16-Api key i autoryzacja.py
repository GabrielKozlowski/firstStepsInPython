# ##***Wysyłanie autoryzacji api-key, losowanie losowego kotka i dodawanie go do ulubionych w subkoncie***
# import requests
# import json
# import credentials
#
# def get_json_content_from_response(response):
#     try:
#         content = response.json()
#     except json.decoder.JSONDecodeError:
#         print("Bad format", response.text)
#     else:
#         return content
#
# def get_favorite_cats(userId):
#     params ={
#         "sub_id" : userId
#     }
#     r = requests.get("https://api.thecatapi.com/v1/favourites",params,
#                      headers=credentials.headers)
#
#     return get_json_content_from_response(r)
#
# def get_random_cat():
#     r = requests.get("https://api.thecatapi.com/v1/images/search",
#                      headers=credentials.headers)
#
#     return get_json_content_from_response(r)
#
# def add_cat_to_favorits(image_id, userId):
#     catData = {
#         "image_id" : image_id,
#         "sub_id" : userId
#     }
#     r = requests.post("https://api.thecatapi.com/v1/favourites/",json=catData,
#                      headers=credentials.headers)
#     return get_json_content_from_response(r)
#
# def show_favorits_cats(favoriteCats):
#     catUrls = []
#     for catId in favoriteCats:
#         catUrl = catId['image']['url']
#         catUrls.append(catUrl)
#
#     return catUrls
#
# userId = "fifka9"
# name = "Gabriel"
#
# print("Witaj " + name)
#
# favoriteCats = get_favorite_cats(userId)
#
#
# print("Twoje ulubione kotki to ", show_favorits_cats(favoriteCats),"\n")
# print("Teraz wylosujemy nowego kotka:\n")
# random_cat = get_random_cat()
# print("Wylosowałeś kotka ", random_cat[0]['url'])
#
# addCatToFavorits = input("Czy chcesz dodać kotka do ulubonych T/N : ")
#
# if (addCatToFavorits.upper() == 'T'):
#     print("Super :D kotek został dodany do ulubionych")
#     add_cat_to_favorits(random_cat[0]['id'], userId)
# else:
#     print("No to kotek będzie smutny :(")
