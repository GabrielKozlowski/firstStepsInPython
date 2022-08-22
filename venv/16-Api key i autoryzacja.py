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
#     return get_json_content_from_response(r)[0]
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
#     for catsData in favoriteCats:
#         catId = catsData['id'],catsData['image']['url']
#         catUrls.append(catId)
#
#     return catUrls
#
# def remove_cat_from_favorits(userId, catNumber):
#     r = requests.delete("https://api.thecatapi.com/v1/favourites/"+catNumber,
#                       headers=credentials.headers)
#
#     return get_json_content_from_response(r)
#
#
# userId = "fifka9"
# name = "Gabriel"
#
# print("Witaj " + name)
#
# favoriteCats = get_favorite_cats(userId)
#
# print("Twoje ulubione kotki to ", show_favorits_cats(favoriteCats),"\n")
# print("Teraz wylosujemy nowego kotka:\n")
#
# random_cat = get_random_cat()
# print("Wylosowałeś kotka", random_cat['url'])
#
#
#
#
# while True:
#     addCatToFavorits = input("Czy chcesz dodać kotka do ulubonych T/N : ")
#     if (addCatToFavorits.upper() == 'T'):
#         resultFromAddingFavoriteCat = add_cat_to_favorits(random_cat['id'], userId)
#         newlyAddedCatInfo = [resultFromAddingFavoriteCat["id"] , random_cat['url']]
#         print("Super :D kotek został dodany do ulubionych kptków: ", newlyAddedCatInfo + show_favorits_cats(favoriteCats))
#         break
#     elif (addCatToFavorits.upper() == 'N'):
#         print("No to kotek będzie smutny :( ")
#         break
#     else:
#         print("Napisz T albo N")
#         continue
#
#
# while True:
#     removeCatFromFavorits = input("Czy chcesz usunąć z ulubionych jakiegoś kotka T/N ")
#     if (removeCatFromFavorits.upper() == 'T'):
#         catNumber = input("Podaj numer kotka którego chcesz usunąć: ")
#         remove_cat_from_favorits(userId, catNumber)
#         print("Kotek usunięty z listy ulubionych")
#         continue
#     elif (removeCatFromFavorits.upper() == 'N'):
#         print("Jesteś super bo lubisz swoje kotki")
#         break
#     else:
#         print("Napisz T albo N")
#         continue
#
