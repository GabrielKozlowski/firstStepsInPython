from result import Ok, Error


class Bankaccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if (self.balance > amount):
            self.balance -= amount
            return Ok("Tak wypłacono kasę", amount)

        return Error("Nie wypłacono kasy", amount)

    def __str__(self):
        return str(self.balance)


class MinimumBalanceAccount(Bankaccount):
    def __init__(self, balance=0, minimumBalance=1000):
        super().__init__(balance)
        self.minimumBalance = minimumBalance

    def withdraw(self, amount):
        if (self.balance - amount >= self.minimumBalance):
            return super().withdraw(amount)
        else:
            return Error("Nie udało się , próba przekroczenia progu", amount)
