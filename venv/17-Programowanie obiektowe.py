"""
OOP - Object Oriented Programming

Programowanie zorientowane wokół obiektów

OBIEKT

OBIEKTY - to pojemniki do przechowywania zmiennych i funkcji tematycznnie ze
          sobą powiązanych do dalszego łatwiejszego ponownego użycia

Klasy - foremki (szablony) do tworzenia egzemplarzy obiektów

Atrybuty - cecha opisująca obiekt
Metoda - funkcja, która operuje na obiekcie

Instancja klasy - instancja  ang. egzemplarz to obiekt, który wyszedł z formy (klasy)


"""


class User:
    age = 0,
    height = 0,


seba = User()
seba.age = 16
seba.height = 183

mirek = User()
mirek.age = 24
mirek.height = 179


# seba.age = 16
# seba.height = 183
#
# mirek.age = 24
# mirek.height = 179

print(seba.age)
print(seba.height)
print(mirek.age)
print(mirek.height)

