# """
# OOP - Object Oriented Programming
#
# Programowanie zorientowane wokół obiektów
#
# OBIEKT
#
# OBIEKTY - to pojemniki do przechowywania zmiennych i funkcji tematycznnie ze
#           sobą powiązanych do dalszego łatwiejszego ponownego użycia
#
# Klasy - foremki (szablony) do tworzenia egzemplarzy obiektów
#
# Atrybuty - cecha opisująca obiekt
# Metoda - funkcja, która operuje na obiekcie
#
# Instancja klasy - instancja  ang. egzemplarz to obiekt, który wyszedł z formy (klasy)
#
#
# __init__ - initialization - inicjalizacja - zyli ustawienie startowych
#            wartości dla atrybutów
#
# w innych językach __init__ to konstruktor
#
# """
#
#
# """
# -klasa , stwórz rakietę która leci do góry.
# -stwórz atrybuty i metody
# -stwórz 5 instancji /klasy /obiektów "rocket" o startowej wysokości 0
# -porusz wszystkie rakiety 10x losowo do góry i wypisz wysokości wszystkich rakiet
#
# """
#
#
#
#
# import random
# class Rocket:
#
#     def __init__(self):
#
#         self.height = 0
#
#     def move_up(self):
#
#         self.height += 1
#
#
#
# rockets = [Rocket() for _ in range(5)]
#
# for _ in range(10):
#     rocketIndexToMove = random.randint(0, 4)
#     rockets[rocketIndexToMove].move_up()
#
#
# for rocket in rockets:
#     print(rocket.height)
# ##-----------------------------------------------------------------------
#
# from random import randint
# class Rocket:
#
#     def __init__(self):
#
#         self.altitude = 0
#
#     def moveUp(self):
#
#         self.altitude += 1
#
#
# rockets = [Rocket() for _ in range(5)]
#
# for _ in range(10):
#     rocketIndexToMove = randint(0,4)
#     rockets[rocketIndexToMove].moveUp()
#
# for rocket in rockets:
#     print(rocket.altitude)
#
# ##---------------------------------------------------------------
# from random import randint
#
# class Rocket:
#
#     def __init__(self, speed):
#
#         self.altitude = 0
#         self.speed = speed
#
#     def moveUp(self):
#
#         self.altitude += self.speed
#
# rocketSpeed = randint(10,50)
# rockets = [Rocket(rocketSpeed) for _ in range(5)]
#
# for _ in range(10):
#     numberOfRocket = randint(0,4)
#     rockets[numberOfRocket].moveUp()
#
# for rocket in rockets:
#     print(rocket.altitude)
#
# ##-------------------------------------------------------------------------