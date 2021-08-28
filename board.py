import numpy as np


class Board():
    def __init__(self,player1,player2):
        self.b = np.zeros((3, 3))
        self.p1 = player1
        self.p2 = player2

    def availableMoves(self):
        board = self.b
        return np.argwhere(board == 0)

    def checkWin(self):
        board = self.b
        best = max(list(board.sum(axis=0)) +  # columns
                   list(board.sum(axis=1)) +  # rows
                   [board.trace()] +  # main diagonal
                   [np.fliplr(board).trace()],  # other diagonal
                   key=abs)
        if abs(best) == board.shape[0]:  # assumes square board
            return np.sign(best)  # winning player, +1 or -1
        if self.availableMoves().size == 0:
            return 0  # a draw (otherwise, return None by default)

    def play(self):
        self.b = np.zeros((3, 3))
        while self.checkWin() is None:
            move = self.p1.move(self.b)
            self.b[tuple(move)] = self.p1.id
            # print(self.b)
            if self.checkWin() is not None:
                break
            move = self.p2.move(self.b)
            self.b[tuple(move)] = self.p2.id
            # print(self.b)
        return self.checkWin()

    def playGames(self,number_of_games):
        results_dict = {-1: 0, 1: 0, 0: 0}
        for i in range(number_of_games):
            resultOfGame = int(self.play())
            results_dict[resultOfGame] +=1
        return results_dict


