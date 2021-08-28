import numpy as np
import random

class Player():

    def move(self):
        pass


class RandomPlayer(Player):
    def __init__(self, id):
        self.id = id

    def availableMoves(self,board):
        return np.argwhere(board == 0)

    def move(self, board):
        return random.choice(self.availableMoves(board))


class QPlayer(Player):
    def __init__(self,id):
        self.id = id

    def availableMoves(self,board):
        return np.argwhere(board == 0)
