# import time
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
# def function_performance(func,arg):
#     func(arg)
#
# def show_message(message):
#     print(message)
#
# function_performance(show_message,"wiadomości")
#
#
# def function_performance2(func,arg):
#     start = time.perf_counter()
#     func(arg)
#     stop = time.perf_counter()
#     return stop - start
#
#
# print(function_performance2(sumuj_do,500))
# print(function_performance2(sumuj_do2,500))
# print(function_performance2(sumuj_do3,500))
# print(function_performance2(sumuj_do4,500))
# print(function_performance2(sumuj_do5,500))
# -------------------------------------------