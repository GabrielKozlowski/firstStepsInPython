# import time
#
# #komenda time.perf_counter() zaczyna i kończy liczenie czasu
#
#
# def sumuj_do(liczba):
#     suma = 0
#     for liczba in range(1,liczba+1):
#         suma = suma + liczba
#
#     return suma
#
# def sumuj_do2(liczba):
#     return sum([liczba for liczba in range(1,liczba+1)])
#
# def sumuj_do3(liczba):
#     return sum({liczba for liczba in range(1,liczba+1)})
#
# def sumuj_do4(liczba):
#     return sum((liczba for liczba in range(1,liczba+1)))
#
# def sumuj_do5(liczba):
#     return (1 + liczba) / 2 * liczba
#
#
# start = time.perf_counter()
# print(sumuj_do(500))
# stop = time.perf_counter()
# print(stop-start)
#
# start = time.perf_counter()
# print(sumuj_do2(500))
# stop = time.perf_counter()
# print(stop-start)
#
# start = time.perf_counter()
# print(sumuj_do3(500))
# stop = time.perf_counter()
# print(stop-start)
#
# start = time.perf_counter()
# print(sumuj_do4(500))
# stop = time.perf_counter()
# print(stop-start)
#
# start = time.perf_counter()
# print(sumuj_do5(500))
# stop = time.perf_counter()
# print(stop-start)