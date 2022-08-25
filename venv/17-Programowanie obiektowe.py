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
    age = 0
    height = 0
    name = ''

    def print_age(self):
        print('Imie:', self.name, 'wiek:', self.age, 'wzrost:', self.height)


userX = User()
userX.age = 16
userX.height = 183
userX.name = 'Arek'
userX.print_age()

userY = User()
userY.age = 24
userY.height = 179
userY.name = 'Mirek'
userY.print_age()



