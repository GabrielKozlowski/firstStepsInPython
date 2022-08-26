# """
# OOP - Object Oriented Programming

# Programowanie zorientowane wokół obiektów

# OBIEKT

# OBIEKTY - to pojemniki do przechowywania zmiennych i funkcji tematycznnie ze
#           sobą powiązanych do dalszego łatwiejszego ponownego użycia

# Klasy - foremki (szablony) do tworzenia egzemplarzy obiektów

# Atrybuty - cecha opisująca obiekt
# Metoda - funkcja, która operuje na obiekcie

# Instancja klasy - instancja  ang. egzemplarz to obiekt, który wyszedł z formy (klasy)

# """

# class User:
#     age = 0
#     height = 0
#     name = ''

#     def print_age(self):
#         print('Imie:', self.name, 'wiek:', self.age, 'wzrost:', self.height)


# userX = User()
# userX.age = 16
# userX.height = 183
# userX.name = 'Arek'
# userX.print_age()

# userY = User()
# userY.age = 24
# userY.height = 179
# userY.name = 'Mirek'
# userY.print_age()

# ##------------------------------------------------------------------------------------------

# """
# __init__ - initialization - inicjalizacja - zyli ustawienie startowych
#            wartości dla atrybutów

# w innych językach __init__ to konstruktor

# """


# class User:

#     def __init__(self, age, name):
#         print(
#             "jestem inicjalizatorem, ktury wywołuje się zawsze podczas onstrukcji obiektu")
#         self.age = age
#         self.name = name

#         self.ageInFuture = age + 1



#     def print_age(self, message):
#         print(message, 'wiek: ', self.age, self.name)


# user1 = User(30, 'Arek')
# user2 = User(24, 'Mirek')


# user1.print_age("Dodatkowy tekst całkowicie inny")
# user2.print_age("Dodatkowy tekst")


# print(user1.ageInFuture)

##--------------------------------------------------------------------------------------------