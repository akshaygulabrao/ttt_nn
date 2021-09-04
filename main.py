from board import Board
from player import RandomPlayer,QPlayer


b = Board(RandomPlayer(), RandomPlayer())
print(b.playGames(1000))

