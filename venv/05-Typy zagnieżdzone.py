#
# # łączenie setów z krotkami w środku
# listaGosci = {
#     ('Arkadiusz', 28, 'mężczyzna'),
#     ('Wioletta', 26, 'kobieta'),
#     ('Kuba', 32, 'mężczyzna')
#              }
#
# listaGosci2 = {
#     ('Arkadiusz', 28, 'mężczyzna'),
#     ('W', 26, 'kobieta'),
#     ('K', 32, 'mężczyzna')
#               }
#
# listaGosci3 = listaGosci | listaGosci2 #  | - łączenie bez powtarzania, & - sprawdzanie powtórzeń
#                                        #  ^ - usówanie powtórzę , - odejmowanie powtórzeń w pierwszym secie
#
# print(listaGosci3)

#-------------------------------------------------------------------------------------------------------------------



#
# listaGosci = {
#     ('Arkadiusz', 28, 'mężczyzna',793928723),
#     ('Wioletta', 26, 'kobieta',793201983),
#     ('Kuba', 32, 'mężczyzna',505321359)
# }
#
# listaGosci2 = {
#     ('Arkadiusz', 28, 'mężczyzna',793928723),
#     ('Wiktoria', 26, 'kobieta',668473298),
#     ('Karol', 32, 'mężczyzna',544302983)
# }
#
# listaGosci3 = listaGosci | listaGosci2
# # dodawanie zmiennych w secie po przez pętle for
# for imie,wiek,plec,telefon in listaGosci3:
#     print('Imię ', imie)
#     print('Wiek ', wiek)
#     print('Płeć ', plec)
#     print('Telefon ', telefon)
#     print('\n')
#
#
people = {
        "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
        "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
        "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
        "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
        "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
        "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
        "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
        "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},
         }
#
# people2 = [
#          {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'John', 'age': 27, 'sex': 'Male'},
#          {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
#          {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Agness', 'age': 25, 'sex': 'Female'}
#         ]
#
#
# people3 = ["Arkadiusz",
#            "Wiola",
#            "Kuba"
#           ]
# ratings1 = {
#             "Arkadiusz": (2,1,2,3,2,3),
#             "Agness": (4,2,1,3,4)
# }
# ratings2 = [
#         {'name': "Arkadiusz", 'ratings': (2,1,2,3,2,3), 'behaviour': 4},
#         {'name': "Agness", 'ratings': (4,2,1,3,4), 'behaviour': 2}
#     ]
#
# ratings3 = {
#         "Arkadiusz": {'ratings': (2,1,2,3,2,3), 'behaviour': 4},
#         "Agness": {'ratings': (4,2,1,3,4), 'behaviour': 2}
#     }

# ------------------------------------------------
# for key in ratings1:
#     print(key,' : ' ,ratings1[key])
# ----------------------------------------------------
# for dictionery in ratings2:
#     for key in dictionery:
#       print(key,dictionery[key])
#     print()
#----------------------------------------------------
#
# for key in ratings3:
#     print(key)
#     for value in ratings3[key]:
#        print(value, ' - ',ratings3[key][value])
#     print()
#-----------------------------------------------------


# print(people)
# print("\n")
#
# for dictionery in people:
#     print('ID: ', dictionery)
#     for key in people[dictionery]:
#         print(key,people[dictionery][key])
#     print()
#--------------------------------------------------------

# for dictionery in people2:
#     print()
#     for key in dictionery:
#         print(key , ' : ' ,dictionery[key])
# -----------------------------------------------------------

# for key in people3:
#     print(key)
#--------------------------------

#
# print(people.items())
#
# for id, dictionary in people.items():
#     print("Id :" ,id)
#     for key in dictionary:
#         print(key , " : ", dictionary[key])
#     print()
#----------------------------------------------------