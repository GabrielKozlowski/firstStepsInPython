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


from bankaccount import MinimumBalanceAccount

accountMin = MinimumBalanceAccount(1500, 1000)

result = accountMin.withdraw(500)
print(result.message)