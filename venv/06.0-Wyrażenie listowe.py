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