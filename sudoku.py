class sudokuGame:

    def __init__(self, board:[]):
        self.board = board

    def getSubgrid(self, x:int): # x must be between 0-8
        subgrids = {
            0 : self.getThreeByThreeArea(0,0),
            1 : self.getThreeByThreeArea(3,0),
            2 : self.getThreeByThreeArea(6,0),
            3 : self.getThreeByThreeArea(0,3)

        }
        return subgrids.get(x)


        
    def getThreeByThreeArea(self, x:int, y:int): # x and y are the top left of the area
        if 0 > x  or x >= 7 or 0 > y  or y >= 7:
            raise IndexError("getThreeByThreeArea() parameters are out of bounds")
        valuesInSubgrid = []
        for row in self.board[y:y+3]:
            for i in range(x,x+3):
                valuesInSubgrid.append(row[i])
        return valuesInSubgrid
    
    def printBoard(self): # TODO: add lines that seperate subgrids
        for row in self.board:
            print(row)

