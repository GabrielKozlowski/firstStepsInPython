# from rocket import RocketBoard


# board = RocketBoard()

# board.rockets[0].altitude = 40
# print(board.rockets[0].altitude)
# board[1] = 60
# print(board[1])
#------------------------------------------------


from bankaccount import Bankaccount

# bank = Bankaccount()

# bank.deposit(100)
# bank.deposit(100)
# bank.deposit(100)
# print(Bankaccount.balance)
# bank.withdraw(50)
# print(Bankaccount.balance)

bank = Bankaccount()

bank.deposit(500)
bank.withdraw(200)

print(bank)