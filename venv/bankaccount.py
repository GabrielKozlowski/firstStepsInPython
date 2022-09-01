# Zrobione po mojemu
# class Bankaccount:
#     balance = 0

#     def __init__(self):
#         self.balance = Bankaccount.balance

#     def deposit(self, money=0):
#         self.money = money
#         Bankaccount.balance += self.money

#     def withdraw(self, money=0):
#         self.money = money
#         Bankaccount.balance -= self.money

#     def __str__(self):
#         return str(self.balance)

class Bankaccount:

    def __init__(self):
        self.balance = 0

    def deposit(self, amound):
        self.balance += amound

    def withdraw(self, amound):
        if self.balance > amound:
            self.balance -= amound
        else:
            return "You're a bankrupt"

    def __str__(self):
        return str(self.balance)
