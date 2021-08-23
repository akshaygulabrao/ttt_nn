class Player():

    def move(self):
        pass

class RandomPlayer():
    def __init__(self, id):
        self.id = id

    def move(self, board):
        return