class sudokuGame:

    def __init__(self, board:[]): # takes a 9x9 2D arrayList as board
        self.board = board

    def isSectionComplete(self, list:[]):
        if len(list) != 9:
            raise IndexError("arrayList passed to isComplete() must have a length of 9")
        
        digit_set = set() #create a new set to store unique digits 

        for num in list:
            if 1 <= num <= 9: 
                digit_set.add(num)
    
        return len(digit_set) == 9 

    def getRow(self, i:int):
        return self.board[i]
    
    def getColumn(self, i:int):
        valuesInColumn = []
        for row in self.board:
            valuesInColumn.append(row[i])
        return valuesInColumn

    def getSubgrid(self, x:int): # x must be between 0-8
        if x >= 0 and x <= 8:
            subgrids = { 
                0 : self.getThreeByThreeArea(0,0),
                1 : self.getThreeByThreeArea(3,0),
                2 : self.getThreeByThreeArea(6,0),
                3 : self.getThreeByThreeArea(0,3),
                4 : self.getThreeByThreeArea(3,3),
                5 : self.getThreeByThreeArea(6,3),
                6 : self.getThreeByThreeArea(0,6),
                7 : self.getThreeByThreeArea(3,6),
                8 : self.getThreeByThreeArea(6,6)
            }
            return subgrids.get(x)
        else:
            raise IndexError("getSubgrid() parameter out of bounds, must be 0-8")
        
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

