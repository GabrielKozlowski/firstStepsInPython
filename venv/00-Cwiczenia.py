# Program do zapisywania definicji do kluczy w słownik

# definicje = {}
#
# l = '''
# 1 - Dodawanie nowej definicji
# 2 - Szukaj istniejącej definicji
# 3 - Usunąć wybraną definicję
# 4 - Exit
# '''
#
#
#
# while True:
#     print(l)
#     chose = input("Witaj w programie wybierz odpowiedni numerek ")
#     if chose == '1':
#         klucz = str(input("Podaj klucz słowa definiowanego : "))
#         definicja = str(input("Podaj nową definicję : "))
#         definicje[klucz] = definicja
#         print("Dodano nową definicję :) ")
#
#
#     elif chose == '2':
#         klucz = input("Podaj nazwę szukanej definicji : ")
#         if klucz in definicje:
#             print(definicje[klucz])
#         else:
#             print("Nie znaleźiono definicji o nazwie [ ", klucz," ]")
#
#
#
#
#
#     elif chose == '3':
#         klucz = input("Podaj nazwę definicji do usunięcia : ")
#         if klucz in definicje:
#             del definicje[klucz]
#             print("Usunięto definicję ", klucz)
#         else:
#             print("Nie znaleziono definicji o nazwie [ ",klucz," ]")
#
#
#     elif chose == '4':
#         break
#
#     else:
#         print("Podaj odpowiedni numerek")
#     print()
#
#
#
# print("Koniec Programu")
#------------------------------------------------------------------------------------
#
# liczby = [1,2,3,4,5,6]
#
# potegiDwojki = []
# for element in liczby:
#     potegiDwojki.append(element**2)
#
# liczbyParzyste = []
# for element in liczby:
#     if element %  2 == 0:
#         liczbyParzyste.append(element)
#
# # wzrażenie listowe przyspiesza pętle i jest ładniejsze i krótsze
# potegiDwojki2 = [element**2
#                  for element in liczby
#                 ]
#
# liczbyParzyste2 =[element
#                   for element in liczby
#                   if element %  2 == 0
#                  ]
#
#print(potegiDwojki)
#print(potegiDwojki2)
#
#print(liczbyParzyste)
#print(liczbyParzyste2)
#--------------------------------------------------------------------------------------
#Wrażenia generowane, generują dane nie zapisując ich i nie obciążając pamięci
#
# import sys
# evenNumbers = [element
#                for element in range(400)
#                if element % 2 == 0
#               ]
#
# evenNumbersGenerator = (element
#                         for element in range(400)
#                         if element % 2 == 0
#                        )
# print(sum(evenNumbersGenerator))
# print(evenNumbersGenerator)
# print(sys.getsizeof(evenNumbers))
#
# potegiLiczb = (liczby**2
#                for liczby in range(101)
#               )
# print(potegiLiczb)
# print(sum(potegiLiczb))
#---------------------------------------------------------------------------


#Generator
#
# liczby = (
#     liczba
#     for liczba in range(100,471)
#     if liczba % 7 == 0
#     if liczba % 5 != 0
# )
# for liczba in liczby:
#     print(liczba)
#


#Listowy

# liczby = [
#     liczba
#     for liczba in range(100,471)
#     if liczba % 7 == 0
#     if liczba % 5 != 0
#        ]
#
# print(liczby)
#---------------------------------------------------------------------------

#Program do obliczania pola figur

# import figury
#
#
# menu = '''
# Witaj w menu liczenia powieszchni figur.
#
# 1- Prostokąt
# 2- Kwadrat
# 3- Trójkąt
# 4- Trapez
# 5- Koło
# 6- Koniec
# '''
#
#
#
# while True:
#     print(menu)
#     x = input("Wybierz liczbę figury którerą chcesz obliczyć : ")
#     if x == '1':
#         A = int(input('Podaj wartość boku A do obliczenia : '))
#         B = int(input('Podaj wartość boku B do obliczenia : '))
#         print('Pole prostokąta wynosi : ',figury.pole_prostokata(A,B))
#     elif x == '2':
#         A = int(input('Podaj wartość boku A do obliczenia : '))
#         print('Pole kwadratu wynosi : ', figury.pole_kwadratu(A))
#     elif x == '3':
#         A = int(input('Podaj wartość podstawy A do obliczenia : '))
#         h = int(input('Podaj wartość wysokości h do obliczenia : '))
#         print('Pole trójkąta wynosi : ', figury.pole_trojkata(A, h))
#     elif x =='4':
#         A = int(input('Podaj wartość boku A do obliczenia : '))
#         B = int(input('Podaj wartość boku B do obliczenia : '))
#         h = int(input('Podaj wartość wysokości h do obliczenia : '))
#         print('Pole trapezu wynosi : ', figury.pole_trapezu(A, B, h))
#     elif x == '5':
#         r = int(input('Podaj wartość promienia r do obliczenia : '))
#         print('Pole koła wynosi : ', figury.pole_kola(r))
#     elif x == '6':
#         break
#     else:
#         print("Podano złą liczbę")
# print("Koniec programu")

# ---------------------------------------------------------------------------
# import time
#
# def function_performance2(func,arg, how_many_times = 1):
#     sum = 0
#     for i in range(0,how_many_times):
#         start = time.perf_counter()
#         func(arg)
#         end = time.perf_counter()
#         sum = sum + (end-start)
#     return sum
#
#
#
#
# setContener1 = {i for i in range(1000)}
# listContener1 = [i for i in range(1000)]
#
#
# def isElementIn(what_value):
#     if what_value in listContener1:
#         return True
#     else:
#         return False
#
#
#
# print(function_performance2(isElementIn,1,how_many_times = 500000))

#---------------------------------------------------------------------
# def count(*numbers):
#     a = sum(numbers)
#     return a
#
# print(count(2,4,1,2,4,5,10))
# ------------------------------------


#
#
# a = 4
# print(id(a))
# b = a
# print(id(b))
# b = 7
# print(id(b))
# listSimple = [ 1,4,512,24]
# print(id(listSimple))
# listSample2 = listSimple
# print(id(listSample2))
#
# listSample2.append(465)
# print(id(listSimple))
# print(id(listSample2))
# print("\n")
#
# c = 5
# def add(c,amound = 1):
#     print(c)
#     print(id(c))
#     c = c + amound
#     print(c)
#     print(id(c))
#
#
# add(c)
# print(c)
#
# def append_element_to_list(listka,element):
#     print(id(listka))
#     listka.append(element)
#     print(id(listka))
#
#
# print(listSimple)
# print(id(listSimple))
# append_element_to_list(listSimple,5)
# print(listSimple)
# print(id(listSimple))
# --------------------------------------------
# my_list = [2,3,6,5,8,7,234,65,68,977,77]
#
# my_list_filtreded = list(filter(lambda x: x % 2 == 0, my_list))
# my_list_filtreded2 = [x for x in my_list if x % 2 == 0]
#
# print(my_list_filtreded)
# print(my_list_filtreded2)
#
# -------------------------------------------------
#
#
# import time
#
# liczenieSumy1000liczb = [x for x in range(1,1001)]
#
# def liczenieSumy1000liczb2(ilosc):
#     for x in range(1,ilosc+1):
#         x += 1
#     return x
#
#
# def sumaLiczb(*x):
#     a = sum(x)
#     print(a)
#     return a
#
#
#
#
#
# def testCzasuFunkcji(func,arg):
#     start = time.perf_counter()
#     func(arg)
#     end = time.perf_counter()
#     return (end - start)
#
# print(testCzasuFunkcji(sumaLiczb,4000))
# print(testCzasuFunkcji(liczenieSumy1000liczb2,10000))
#
# ------------------------------------------------------------
# Randomowe losowanie liczb lotto
# import random
#
# lotteryNumbers = []
#
# def chose_random_numbers(amound, total_amound):
#     random.randint(0,total_amound)
#
# while len(lotteryNumbers) < 7:
#     x = random.randint(0,49)
#     if x in lotteryNumbers:
#         continue
#     else:
#         lotteryNumbers.append(x)
#
# print(lotteryNumbers)
#
# ----------------------------------------------------

# # *** Losowanie randomowych pieciu kart do gry w wojnę ***
# import random
# cardList = ['9(♣)','9(♦)','9(♥)','9(♠)',
#             '10(♣)','10(♦)','10(♥)','10(♠)',
#             'J(♣)','J(♦)','J(♥)','J(♠)',
#             'Q(♣)','Q(♦)','Q(♥)','Q(♠)',
#             'K(♣)','K(♦)','K(♥)','K(♠)',
#             'A(♣)','A(♦)','A(♥)','A(♠)']
#
#
# random.shuffle(cardList)
# playerOneCards = []
# playerTwoCards = []
#
# for i in range(5):
#     a = cardList.pop()
#     b = cardList.pop()
#     playerOneCards.append(a)
#     playerTwoCards.append(b)
#
# print(playerOneCards)
# print(playerTwoCards)
#
# --------------------------------------










