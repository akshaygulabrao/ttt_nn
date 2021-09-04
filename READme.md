# Tic Tac Toe Neural Network

## Board
* init(self,player1,player2): Creates the game board(np.zeros((3,3))) and initializes the players
* availableMoves: available moves are marked by 0 in the game board
* checkWin: returns None while the game is ongoing, or the ID of the player that wins OR 0
* playGames: specify an amount of games to be played and the simulation will run automatically

## Player
* id can only be -1 or 1, so I need to use this to make the abstraction much easier
* class with abstract method move()

## RandomPlayer
* move returns a random spot on the board


##QPlayer