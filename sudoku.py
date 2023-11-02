class sudokuGame:

    def __init__(self, board):
        self.board = board

    # def getSubgrid(self, x): # x must be between 0-8
        
    def getThreeByThreeArea(self, x, y): # x and y refer to the top left part of the area being returned
        valuesInSubgrid = []
        for row in self.board[x:x+3]:
            for i in range(y,y+3):
                valuesInSubgrid.append(row[i])
        return valuesInSubgrid
    
    def printBoard(self): # TODO: add lines that seperate subgrids
        for row in self.board:
            print(row)

