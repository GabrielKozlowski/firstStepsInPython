# #Sup klasy korzystające z super klas
# klasy obliczają pole powierzchni i objętość


# class Ractangle():
#     def __init__(self, heigh, width):
#         self.heigh = heigh
#         self.width = width

#     def count_surface_area(self):
#         return self.heigh * self.width


# class Square(Ractangle):
#     def __init__(self, sideLength):
#         super().__init__(sideLength, sideLength)


# class Cube():
#     def __init__(self, square: Square):
#         self.square = square
#         self.height = square.heigh

#     def count_surface_area(self):
#         return self.square.count_surface_area() * 6

#     def count_volume(self):
#         return self.square.count_surface_area() * self.height


# class Cuboid():
#     def __init__(self, figure, height):
#         self.base = figure
#         self.height = height

#     def count_volume(self):
#         return self.base.count_surface_area() * self.height


# ract = Ractangle(5, 10)
# squa = Square(5)
# cube = Cube(Square(5))
# cuboid = Cuboid(Ractangle(2, 3), 4)

# print(squa.count_surface_area())
# print(ract.count_surface_area())
# print(cube.count_surface_area())
# print(cube.count_volume())
# print(cuboid.count_volume())
# # #----------------------------------------------------
# # Super klasy w formie konta bankowego


# from result import Ok, Error


# class Bankaccount:
#     def __init__(self, balance=0):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if (self.balance > amount):
#             self.balance -= amount
#             return Ok("Tak wypłacono kasę", amount)

#         return Error("Nie wypłacono kasy", amount)

#     def __str__(self):
#         return str(self.balance)


# class MinimumBalanceAccount(Bankaccount):
#     def __init__(self, balance=0, minimumBalance=1000):
#         super().__init__(balance)
#         self.minimumBalance = minimumBalance

#     def withdraw(self, amount):
#         if (self.balance - amount >= self.minimumBalance):
#             return super().withdraw(amount)
#         else:
#             return Error("Nie udało się , próba przekroczenia progu", amount)
