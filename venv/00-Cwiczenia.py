# #***Program do zapisywania definicji do kluczy w słownik***
#
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



# print("Koniec Programu")
# #------------------------------------------------------------------------------------

# liczby = [1,2,3,4,5,6]

# potegiDwojki = []
# for element in liczby:
#     potegiDwojki.append(element**2)

# liczbyParzyste = []
# for element in liczby:
#     if element %  2 == 0:
#         liczbyParzyste.append(element)

# #***wyrażenie listowe przyspiesza pętle i jest ładniejsze i krótsze***
# potegiDwojki2 = [element**2
#                  for element in liczby
#                 ]

# liczbyParzyste2 =[element
#                   for element in liczby
#                   if element %  2 == 0
#                  ]

# print(potegiDwojki)
# print(potegiDwojki2)

# print(liczbyParzyste)
# print(liczbyParzyste2)
# #--------------------------------------------------------------------------------------
# #***Wyrażenia generowane, generują dane nie zapisując ich i nie obciążając pamięci***

# import sys
# evenNumbers = [element
#                for element in range(400)
#                if element % 2 == 0
#               ]

# evenNumbersGenerator = (element
#                         for element in range(400)
#                         if element % 2 == 0
#                        )
# print(sum(evenNumbersGenerator))
# print(evenNumbersGenerator)
# print(sys.getsizeof(evenNumbers))

# potegiLiczb = (liczby**2
#                for liczby in range(101)
#               )
# print(potegiLiczb)
# print(sum(potegiLiczb))
# #---------------------------------------------------------------------------


# #***Generator***

# liczby = (
#     liczba
#     for liczba in range(100,471)
#     if liczba % 7 == 0
#     if liczba % 5 != 0
# )
# for liczba in liczby:
#     print(liczba)



# #Listowy

# liczby = [
#     liczba
#     for liczba in range(100,471)
#     if liczba % 7 == 0
#     if liczba % 5 != 0
#        ]

# print(liczby)
# #---------------------------------------------------------------------------

# #***Program do obliczania pola figur***

# import figury


# menu = '''
# Witaj w menu liczenia powieszchni figur.

# 1- Prostokąt
# 2- Kwadrat
# 3- Trójkąt
# 4- Trapez
# 5- Koło
# 6- Koniec
# '''



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

# #---------------------------------------------------------------------------
# import time

# def function_performance2(func,arg, how_many_times = 1):
#     sum = 0
#     for i in range(0,how_many_times):
#         start = time.perf_counter()
#         func(arg)
#         end = time.perf_counter()
#         sum = sum + (end-start)
#     return sum




# setContener1 = {i for i in range(1000)}
# listContener1 = [i for i in range(1000)]


# def isElementIn(what_value):
#     if what_value in listContener1:
#         return True
#     else:
#         return False



# print(function_performance2(isElementIn,1,how_many_times = 500000))

# #---------------------------------------------------------------------
# def count(*numbers):
#     a = sum(numbers)
#     return a

# print(count(2,4,1,2,4,5,10))
# #------------------------------------




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

# listSample2.append(465)
# print(id(listSimple))
# print(id(listSample2))
# print("\n")

# c = 5
# def add(c,amound = 1):
#     print(c)
#     print(id(c))
#     c = c + amound
#     print(c)
#     print(id(c))


# add(c)
# print(c)

# def append_element_to_list(listka,element):
#     print(id(listka))
#     listka.append(element)
#     print(id(listka))


# print(listSimple)
# print(id(listSimple))
# append_element_to_list(listSimple,5)
# print(listSimple)
# print(id(listSimple))
# #--------------------------------------------
# my_list = [2,3,6,5,8,7,234,65,68,977,77]

# my_list_filtreded = list(filter(lambda x: x % 2 == 0, my_list))
# my_list_filtreded2 = [x for x in my_list if x % 2 == 0]

# print(my_list_filtreded)
# print(my_list_filtreded2)

# #-------------------------------------------------


# import time

# liczenieSumy1000liczb = [x for x in range(1,1001)]

# def liczenieSumy1000liczb2(ilosc):
#     for x in range(1,ilosc+1):
#         x += 1
#     return x


# def sumaLiczb(*x):
#     a = sum(x)
#     print(a)
#     return a





# def testCzasuFunkcji(func,arg):
#     start = time.perf_counter()
#     func(arg)
#     end = time.perf_counter()
#     return (end - start)

# print(testCzasuFunkcji(sumaLiczb,4000))
# print(testCzasuFunkcji(liczenieSumy1000liczb2,10000))

# #-----------------------------------------------------------
# #***Randomowe losowanie liczb lotto***
# import random

# lotteryNumbers = []

# def chose_random_numbers(amound, total_amound):
#     random.randint(0,total_amound)

# while len(lotteryNumbers) < 7:
#     x = random.randint(0,49)
#     if x in lotteryNumbers:
#         continue
#     else:
#         lotteryNumbers.append(x)

# print(lotteryNumbers)

# #----------------------------------------------------

# # *** Losowanie randomowych pieciu kart do gry w wojnę ***
# import random
# cardList = ['9(♣)','9(♦)','9(♥)','9(♠)',
#             '10(♣)','10(♦)','10(♥)','10(♠)',
#             'J(♣)','J(♦)','J(♥)','J(♠)',
#             'Q(♣)','Q(♦)','Q(♥)','Q(♠)',
#             'K(♣)','K(♦)','K(♥)','K(♠)',
#             'A(♣)','A(♦)','A(♥)','A(♠)']


# random.shuffle(cardList)
# playerOneCards = []
# playerTwoCards = []

# for i in range(5):
#     a = cardList.pop()
#     b = cardList.pop()
#     playerOneCards.append(a)
#     playerTwoCards.append(b)

# print(playerOneCards)
# print(playerTwoCards)

# #--------------------------------------
# #***Gra która imituje 5 ruchów w kturych można znaleźć skrzykę ze złotem***
# import random
# chanseChest = ["Chest","Nothing"]
# colorOfChest = ["Green","Orange","Purple","Gold"]
# gameLenght = 5
# gold = 0
# choseDirection = 0

# print("Welcome in my game, You be serch a chest with gold. You have only 5 steps \n")



# for move in range(gameLenght):
#     playerChose = input("Chose the direction [forward, left, right, back] : ")
#     steps = random.choices(chanseChest, [6, 4], k=1)
#     step = str(steps.pop())
#     if step == "Chest":
#         colorChests = random.choices(colorOfChest, [75,20,4,1] , k=100)
#         colorChest = str(colorChests.pop())
#         if colorChest == "Green":
#             print("Move : [",move+1,"] You found the chest!! - Its green chest, You get 1000 gold")
#             gold += 1000
#         elif colorChest == "Orange":
#             print("Move : [",move+1,"] You found the chest!! - Its orange chest, You get 4000 gold")
#             gold += 4000
#         elif colorChest == "Purple":
#             print("Move : [",move+1,"] You found the chest!! - Its purple chest, You get 9000 gold")
#             gold += 9000
#         elif colorChest == "Gold":
#             print("Move : [", move+1,"] You found the chest!! - Its gold chest, You get 16000 gold")
#             gold += 16000
#     else:
#         print("Move : [",move + 1 ,"] There is nothing here")

# print("\nYou have :", gold , "in your pocket")
# #------------------------------------------------------------------
# #***Bardziej zaawansowany code do tej samej gry***

# import random
# from enum import Enum

# Event = Enum('Event', ['Chest','Nothing'])

# eventDictionary = {
#                     Event.Chest: 0.6,
#                     Event.Nothing: 0.4
#                   }

# eventList = list(eventDictionary.keys())
# evenProbability = list(eventDictionary.values())
# Colours = Enum('Colours', {'Green' : 'green',
#                            'Orange' : 'orange',
#                            'Purple' : 'purple',
#                            'Gold' : 'gold'
#                            }
#                )
# chestColoursDictionary = {
#                Colours.Green: 0.75,
#                Colours.Orange: 0.20,
#                Colours.Purple: 0.04,
#                Colours.Gold: 0.01
#                           }

# chestColourList = list(chestColoursDictionary.keys())
# chestColourProbability = list(chestColoursDictionary.values())
# rewardsForChests = {
#                     chestColourList[reward]: (reward + 1) * (reward +1) * 1000
#                     for reward in range(len(chestColourList))
# }
# gameLenght = 5
# goldAcquired = 0
# print("""Welome in my game
# You have only 5 steps to make,
# see yourself haw mach gold you gonna acquire till the end!""")


# while gameLenght > 0:
#     gamerAnswer = input("Do you want move? : ")
#     if gamerAnswer == 'yes':
#         print("Great, let's see what you got ...")
#         drawnEvent = random.choices(eventList,evenProbability)[0]
#         if drawnEvent == Event.Chest:
#             drawnColour = random.choices(chestColourList,chestColourProbability)[0]
#             print("Nice, you find a ",drawnColour.value," chest")
#             gamerReward = rewardsForChests[drawnColour]
#             goldAcquired = goldAcquired + gamerReward
#         elif drawnEvent == Event.Nothing:
#             print("Nothing in here.")
#     else:
#         print("If you wanna play, you must write yes")
#         continue
#     gameLenght = gameLenght - 1

# print("Congratulation, you have acquired : ",goldAcquired)
# #----------------------------------------------------------------------

# #***Otwarcie pliku z imionami i nazwiskami, zapisanie imion i nazwisk w innych plikach***


# namesAndSurnames = []

# with open("imionanazwiska.txt","r+",encoding="UTF-8") as file:
#     for line in file:
#         namesAndSurnames.append(tuple(line.replace("\n","").split(" ")))

# with open("imiona.txt", "w", encoding="UTF-8") as file:
#     for item in namesAndSurnames:
#         file.write(item[0] + "\n")

# with open("nazwiska.txt", "w", encoding="UTF-8") as file:
#     for item in namesAndSurnames:
#         try:
#             file.write(item[1] + "\n")
#         except IndexError:
#             file.write("\n")
# #***Otwieranie i sprawdzanie co znajduje się w plikach imiona i nazwiska***
# with open("imiona.txt","r",encoding="UTF-8") as file:
#     print(file.read())
# with open("nazwiska.txt","r",encoding="UTF-8") as file:
#     print(file.read())




# def openFileFunkcion():
#     inputNameFile = input("Please write a name of file with you wanna read : ")
#     try:
#         with open(inputNameFile,"r",encoding="UTF-8") as file:
#             inputNameFile = file.read()
#             print(inputNameFile)

#     except FileNotFoundError:
#         print("File not existed")
# #---------------------------------------------------------------
# from funkcja_otwierajaca_pliki import read_content_of_file

# read_content_of_file
# #===========================================================
# from defOpenFile import openFileFunkcion

# openFileFunkcion
# #------------------------------------------------------------------
# #***Nauka pprint***

# import pprint

# stuff = ['spam','eggs','lumberjack','knights','ni']
# stuff.insert(0,stuff[:])

# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(stuff)

# pp = pprint.PrettyPrinter(width=33,compact=True)
# pp.pprint(stuff)

# tup = ('spam',('eggs',('lumberjack',('knights',('ni',('dead',('parrot',('fresh fruits',))))))))

# pp = pprint.PrettyPrinter(depth=6)
# pp.pprint(tup)

# #--------------------------------------------------------------
# #***Wyświetlenie największej wartości ze strony na której jest słownik z kluczami i wartościami w json***
# import requests
# import json
# """
# {
#  1:11
#  2:6
#  3:4
# }
# """


# r = requests.get("https://jsonplaceholder.typicode.com/todos")  ### Strona z zawodnikami i zadniami

# def count_task_frequency(tasks):                          ### Funkcja do wyłapania zaliczonych zadań i przypisania
#     completedTaskFrequencyByUser = dict()                 ### ilosci do użytkownikó
#     for entry in tasks:                                              ### pętla dla wejść w zadania
#         if (entry["completed"] == True):                             ### odniesienie się do value "completed"
#             try:                                                  ### próba do wyciągnięcia błędu dodania do niczego
#                 completedTaskFrequencyByUser[entry["userId"]] += 1
#             except KeyError:
#                 completedTaskFrequencyByUser[entry["userId"]] = 1

#     return completedTaskFrequencyByUser                            ### zwraca listę w której są dodane Keys
#                                                                    ### z wartościami i spełniające if

# def get_users_with_top_completed_tasks(completedTaskFrequencyByUser): ### funkcja wybiera użytkownika z największą
#     userIdWithMaxCompletedAmoundTasks = []                            ### ilością zrobionych zadań
#     maxAmoundOfCompletedTask = max(completedTaskFrequencyByUser.values())  ### przypisanie do zmiennej
#     for userId, numberOfCompletedTsks in completedTaskFrequencyByUser.items():
#         if (numberOfCompletedTsks == maxAmoundOfCompletedTask):
#             userIdWithMaxCompletedAmoundTasks.append(userId)

#     return userIdWithMaxCompletedAmoundTasks


# try:
#     tasks = r.json()
# except json.decoder.JSONDecodeError:
#     print("Niepoprawny format")
# else:
#     completedTaskFrequencyByUser = count_task_frequency(tasks)
#     usersWithTopCompletedTasks = get_users_with_top_completed_tasks(completedTaskFrequencyByUser)
#     print("Wręczamy ciasteczko mistrzunia dyscypliny do użytkowników o id: ", usersWithTopCompletedTasks)
# #-----------------------------------------------------------------
# #***zainportowanie funkcji z pliku i odtworzenie zadania powyżej***
# from functions import get_keys_with_top_values

# get_keys_with_top_values(completedTaskFrequencyByUser)
# #-----------------------------------------------------------

# import requests
# import json



# def count_completed_tasks(tasks):
#     tasksCompleted = dict()
#     for entry in tasks:
#         if (entry["completed"] == True):
#             try:
#                 tasksCompleted[entry["userId"]] += 1
#             except KeyError:
#                 tasksCompleted[entry["userId"]] = 1
#     return tasksCompleted

# def user_with_top_completed_tasks(tasksCompleted):
#     maxCompletedTasks = max(tasksCompleted.values())
#     topScoreUserId = []
#     for userId, score in tasksCompleted.items():
#         if score == maxCompletedTasks:
#             topScoreUserId.append(userId)
#     return topScoreUserId





# webSite = requests.get("https://jsonplaceholder.typicode.com/todos")

# try:
#     tasks = webSite.json()
# except json.decoder.JSONDecodeError:
#     print("Niepoprawny format")
# else:
#     tasksCompleted = count_completed_tasks(tasks)
#     topScoreUserId = user_with_top_completed_tasks(tasksCompleted)
#     print("Najlepsi uźytkownicy to :", topScoreUserId)
# #------------------------------------------------------------------------------------
# #***Tworzenie generatora z funkcji metodą Yield i wywoływanie jej komendą next()***

# def number_multiplied_by_itself_generator():
#     number = 0
#     while True:
#         number += 1
#         sumOfMultiplication = (number * number)
#         yield sumOfMultiplication

# multipliedNumbers = number_multiplied_by_itself_generator()

# def repeat_20_times():
#     numbers = []
#     for _ in range(20):
#         number = next(multipliedNumbers)
#         numbers.append(number)
#     text ="Super teraz poczytam książkę"
#     numbers.append(text)
#     return numbers


# def repeat_30_times():
#     numbers = []
#     for _ in range(30):
#         number = next(multipliedNumbers)
#         numbers.append(number)
#     return numbers

# listOfGeneratedNumbers = repeat_20_times() + repeat_30_times()

# print(listOfGeneratedNumbers)

# #--------------------------------------------------------------------------------


# #***Wysyłanie wartości do generatora , wstawiamy w linie z Yield !***

# def number_multiplied_by_itself_generator():
#     number = 0
#     while True:
#         print("Start number", number)
#         number = yield number * number
#         print("Po yield number", number)


# generatedNumbers = []

# numberGenerator = number_multiplied_by_itself_generator()

# numberGenerator.send(None)

# for i in range(0,20):
#     generatedNumbers.append(numberGenerator.send(i))

# print(generatedNumbers)

# for i in range(20,50):
#     generatedNumbers.append(numberGenerator.send(i))

# print(generatedNumbers)

print("sdsdsds")