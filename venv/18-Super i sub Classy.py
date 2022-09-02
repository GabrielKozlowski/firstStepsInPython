# # #Sup klasy korzystające z super klas
# # klasy obliczają pole powierzchni i objętość


# class Ractangle():
#     def __init__(self, heigh, width):
#         self.heigh = heigh
#         self.width = width

#     def count_surface_area(self):
#         return self.heigh * self.width


# class Square(Ractangle):
#     def __init__(self, sideLength):
#         super().__init__(sideLength, sideLength)


# class Cube(Square):
#     def count_surface_area(self):
#         return super().count_surface_area() * 6

#     def count_volume(self):
#         return super().count_surface_area() * self.heigh


# ract = Ractangle(5, 10)
# squa = Square(5)
# cube = Cube(5)
# print(squa.count_surface_area())
# print(ract.count_surface_area())
# print(cube.count_surface_area())
# print(cube.count_volume())

# #----------------------------------------------------
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
