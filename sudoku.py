class sudokuGame:

    def __init__(self): # creates a new, predetermined board when instantiated
        self.board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

    def getSubgrid(self): # x and y must be 0-3
        valuesInSubgrid = []
        for row in self.board[0:3]:
            for i in range(0,3):
                valuesInSubgrid.append(row[i])
        return valuesInSubgrid


    
    def printBoard(self): # TODO: add lines that seperate subgrids
        for row in self.board:
            print(row)
        
    

myGame = sudokuGame()
# myGame.printBoard()
print(myGame.getSubgrid())
