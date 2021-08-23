from board import Board
from player import RandomPlayer

b = Board(RandomPlayer(1), RandomPlayer(-1))
print(b.checkWin())
