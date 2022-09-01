# Zrobione po mojemu
class Bankaccount:
    balance = 0

    def __init__(self):
        self.balance = Bankaccount.balance

    def deposit(self, money=0):
        self.money = money
        Bankaccount.balance += self.money

    def withdraw(self, money=0):
        self.money = money
        Bankaccount.balance -= self.money

    def __str__(self):
        return str(self.balance)

