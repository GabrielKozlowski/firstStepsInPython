'''
Plik - nazwa lokacji która przechowuje na STAŁE dane na dysku.

Ram - pamięć podręczna komputera, gdzie przechowywane są dane TYMCZASOWE

podstawowe sposoby otwierania plików
r - Read (czytanie) - domyślne
w - Write (pisanie) - jeśli plik istnieje to go usunie, jeśli nie to stworzy
a - Append (dopisywanie)

rozszerzenie to tylko 'tekst' nadawany po to , ady inne programy rozpoznawały
plik w odpowiedni dla tych programów sposób
'''

file = open("testt.txt", "w") # UCHWYT - HANDLE
file.write("simple ")
file.write("simple")
