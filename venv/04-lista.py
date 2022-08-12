# '''
# len() - długość
# .append() - dodać jeden element
# .extend() - rozszerzyć o elementy
# .insert(index,co) - wstawić element na dane miejsce
# .index() - indeks danego elementu
# sort(reverse=false) - sortowanie rosnąco
# max() - podaj największy element
# min() - podaj najmniejszy element
# .count() - podaj ile razy coś występuje w liście
# .pop() - usuń ostatni element z listy
# .remove() - usuń pierwszy element z listy
# .clear() - wyczyść listę
# .reverse() - odwróć kolejność
#
# '''


imiona = []
imiona.append("Wojtek")
imiona.extend(["Adrian", "Kinga", "Bartek", "Asia"])
imiona.insert(2,"Andrzej")
imiona.index("Andrzej")
imiona.sort(reverse=False)
print(imiona)
imiona.sort(reverse=True)
print(imiona)
print(imiona.count("Kinga"))
imiona.pop()
print(imiona)
imiona.remove("Andrzej")
print(imiona)
imiona.clear()
print(imiona)


numery = [2,32,-1,56,4,8,-23,58]
print(max(numery))
print(min(numery))