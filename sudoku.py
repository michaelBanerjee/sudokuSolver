class sudokuGame:

    def __init__(self, board:[]):
        self.board = board

    # def getSubgrid(self, x): # x must be between 0-8
        
    def getThreeByThreeArea(self, x:int, y:int): # x and y refer to the top left part of the area returned
        if 0 > x  or x >= 7 or 0 > y  or y >= 7:
            raise IndexError("getThreeByThreeArea() parameters are out of bounds")
        valuesInSubgrid = []
        for row in self.board[x:x+3]:
            for i in range(y,y+3):
                valuesInSubgrid.append(row[i])
        return valuesInSubgrid
    
    def printBoard(self): # TODO: add lines that seperate subgrids
        for row in self.board:
            print(row)

