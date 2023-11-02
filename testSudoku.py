import unittest
from sudoku import sudokuGame

class testSudoku(unittest.TestCase):
    
    game = sudokuGame()
    
    def testGetSubGrid(self):
        self.assertEqual([5, 3, 0, 6, 0, 0, 0, 9, 8],self.game.getSubgrid())

if __name__ == "__main__":
    unittest.main()