## Pętla wypisuje liczby od 0 do 10
### The loop print numbers from 0 to 10

# i = 0
# while i <= 10:
#     print(i)
#     i += 1
#-----------------------------------------------------------------------------------
## Pętla wypisuje liczby od 100 do 0
### The loop print numbers from 100 to 0

# liczba = 100
# while liczba >= 0:
#     print(liczba)
#     liczba -= 1
#-----------------------------------------------------------------------------------------
##Pętla wykonuje dodawanie 4 liczb od użytkownika i wyświetla wynik
### The loop added 4 numbers from users and print the sum
# wynik = 0
# i = 0
# while i < 4:
#     x = int(input("Podaj liczbę którą chcesz dodać: "))
#     wynik += x
#     i += 1
#
# print("Suma dadanych liczb wynosi: ", wynik)
#--------------------------------------------------------------------------------------
# ## Pętla wypisuje liczby podzielne przez 5 i nie podzielne przez 7 w zakresie 0-200
# # The loop print numbers divisibles by 5 and not divisibles by 7 in range 0-200
# for i in range(0,200):
#     if (i % 5 == 0 and  i % 7 == 1):
#         print(i)
#---------------------------------------------------------------------------------------------
# ## Dodawanie liczb tylko parzystych i tylko dodatnich
# # Adds only a even and positive numbers
# wynik = 0
# i = 0
# while i < 3:
#     x = int(input("Podaj dodatnią i parzystą liczbę: "))
#     if x < 0:
#         print("Miała być liczba dodatnia! , podaj właściwą liczbę ")
#         continue
#     elif x % 2 == 1:
#         print("Miała być liczba parzysta! , podaj właściwą liczbę")
#         continue
#     else:
#         wynik += x
#         i += 1
#
# print("Wynik to ",wynik)
# ------------------------------------------------------------------------------------------
#
#
#
# ##Szukanie odpowiedniej liczby
# #Looking for the right number
#
# szukanaLiczba = 40
# i = 0
# while i < 1:
#     x = int(input("Zgadnij liczbę: "))
#     if x > szukanaLiczba:
#         print("Liczba którą podałeś/aś jest za duża, spróbój ponownie ")
#     elif x < szukanaLiczba:
#         print("Liczba którą podałeś/aś jest za mała, spróbój ponownie ")
#     else:
#         print("Brawo trafiłeś/aś prawidłową liczbę! :)")
#         i += 1
#-------------------------------------------------------------------------------

