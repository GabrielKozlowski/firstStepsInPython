# from rocket import RocketBoard


# board = RocketBoard()

# board.rockets[0].altitude = 40
# print(board.rockets[0].altitude)
# board[1] = 60
# print(board[1])
# ------------------------------------------------

# #------------------------------------------------------
# from bankaccount import Bankaccount

# bank = Bankaccount(500)

# amoundToWitdraw = 700

# result = bank.withdraw(amoundToWitdraw)

# if (result.isSuccess):
#     print(result.message)
# else:
#     print(result.message)
# #---------------------------------------------------------


# from bankaccount import MinimumBalanceAccount

# accountMin = MinimumBalanceAccount(1500, 1000)

# result = accountMin.withdraw(500)
# print(result.message)


"""
    Stwórz trzy klasy:
    1) Ractangle - prostokąt
    2) Sqare - kwadrat
    3) Cube - sześcian

    a) Stwórz konstruktory __init__
    b) metody obliczające powieszchnię prostokąta, kwadratu, sześcianu
    c) metodę obliczającą objętość sześcianu

    zastanów się jak możesz wykorzystać do tego dziedziczenie, aby nie powtarzać kodu
"""


class Ractangle():
    def __init__(self, heigh, width):
        self.heigh = heigh
        self.width = width

    def count_surface_area(self):
        return self.heigh * self.width


class Square(Ractangle):
    def __init__(self, sideLength):
        super().__init__(sideLength, sideLength)


class Cube(Square):
    def count_surface_area(self):
        return super().count_surface_area() * 6

    def count_volume(self):
        return super().count_surface_area() * self.heigh


ract = Ractangle(5, 10)
squa = Square(5)
cube = Cube(5)
print(squa.count_surface_area())
print(ract.count_surface_area())
print(cube.count_surface_area())
print(cube.count_volume())
