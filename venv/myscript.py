from rocket import RocketBoard


board = RocketBoard()

board.rockets[0].altitude = 40
print(board.rockets[0].altitude)
board[1] = 60
print(board[1])

