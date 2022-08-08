# import figury
# #enumeration - spis - wyliczenie
#
# from enum import IntEnum
#
# Menu_Figury = IntEnum('Menu_Figury' ,'Kwadrat Prostokąt Koło Trójkąt Trapez')
#
# wybór = int(input("""Wybierz figurę, której chcesz obliczyć pole:
# 1. Kwadrat
# 2. Prostokąt
# 3. Koło
# 4. Trójkąt
# 5. Trapez
# """))
#
# if (wybór == Menu_Figury.Kwadrat):
#     a = float(input("Podaj bok kwadratu: "))
#     print("Pole kwadratu wynosi: ", figury.pole_kwadratu(a))
# elif (wybór == Menu_Figury.Prostokąt):
#     a = float(input("Podaj 1-wszy bok prostokąta: "))
#     b = float(input("Podaj 2-gi bok prostokąta: "))
#     print("Pole prostokąta wynosi: ", figury.pole_prostokata(a,b))
# elif (wybór == Menu_Figury.Koło):
#     r = float(input("Podaj promień koła: "))
#     print("Pole koła wynosi: ", figury.pole_kola(r))
# elif (wybór == Menu_Figury.Trójkąt):
#     a = float(input("Podaj bok trójkąta: "))
#     h = float(input("Podaj wysokość trójkąta: "))
#     print("Pole trójkąta wynosi: ", figury.pole_trojkata(a,h))
# elif (wybór == Menu_Figury.Trapez):
#     a = float(input("podaj 1-wszy bok trapezu: "))
#     b = float(input("Podaj 2-gi bok trapezu: "))
#     h = float(input("Podaj wysokość trapezu: "))
#     print("Pole trapezu wynosi: ", figury.pole_trapezu(a,b,h))
# else:
#     print("Musisz podać odpowiednią cyfrę")

#-------------------------------------------------------------------------

#
#
#
# from enum import IntEnum
#
# Menu_Kolory = IntEnum('Menu_Kolory','Czerwony Czarny Zielony Niebieski Biały Żółty')
#
# wybór = int(input("""Witaj, wybierz kolor który Ci się podoba
# 1. Czerwony
# 2. Czarny
# 3. Zielony
# 4. Niebieski
# 5. Biały
# 6. Żółty
# """))
#
# if (wybór == Menu_Kolory.Czerwony):
#     print("Twój ulubiony kolor to: Czerwony")
# if (wybór == Menu_Kolory.Czarny):
#     print("Twój ulubiony kolor to: Czarny")
# if (wybór == Menu_Kolory.Zielony):
#     print("Twój ulubiony kolor to: Zielony")
# if (wybór == Menu_Kolory.Niebieski):
#     print("Twój ulubiony kolor to: Niebieski")
# if (wybór == Menu_Kolory.Biały):
#     print("Twój ulubiony kolor to: Biały")
# if (wybór == Menu_Kolory.Żółty):
#     print("Twój ulubiony kolor to: Żółty")
#
# ------------------------------------------------------------------------


