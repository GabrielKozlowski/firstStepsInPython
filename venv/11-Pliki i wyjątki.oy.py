'''
Plik - nazwa lokacji która przechowuje na STAŁE dane na dysku.

Ram - pamięć podręczna komputera, gdzie przechowywane są dane TYMCZASOWE

podstawowe sposoby otwierania plików
r - Read (czytanie) - domyślne
w - Write (pisanie) - jeśli plik istnieje to go usunie, jeśli nie to stworzy
a - Append (dopisywanie)

rozszerzenie to tylko 'tekst' nadawany po to , ady inne programy rozpoznawały
plik w odpowiedni dla tych programów sposób

tell - mów, gdzie skończyliśmy ostatnią operacjęna pliku
seek - szuka (zmienia) - na miejsce wskazania przaz nas

mnogie tryby otwierania plików:
r+ - do czytania i pisania

w+ - do pisania i czytania
różni się tym, że usunie zawartość istniejącego pliku
lub stworzy plik gdyby go nie było

a+ - "Wieczny tryb" dopisywania i przy okazji czytania
UWAGA! wskaźnik dopisywania jest zawsze na końcu jeśli plik nie istniał - stworzy go

'''
# ***Otwieranie , zapisywanie i zamykianie pliku***
# file = open("testt.txt", "w") # UCHWYT - HANDLE
# file.write("simple ")
# file.write("simple")
# file.close()
#

#***Otwieranie i czytanie pliku linijka po linijce***
# with open("oceany.txt", "r",encoding="UTF-8") as file:
#     oceany = file.read().splitlines()
#     print(oceany)
# print("\n")
# with open("oceany.txt","r",encoding="UTF-8") as file:
#     for line in file:
#         print(line)


#***Dodawanie do pliku na koniec***
# with open("oceany.txt","a",encoding="UTF-8") as file:
#     file.write("Południowy")

