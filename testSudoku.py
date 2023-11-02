import unittest
from sudoku import sudokuGame

class testSudoku(unittest.TestCase):
    board = [
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
    game = sudokuGame(board)
    
    def testGetThreeByThreeArea(self):
        self.assertEqual([5, 3, 0, 6, 0, 0, 0, 9, 8], self.game.getThreeByThreeArea(0,0))
        self.assertEqual([8, 0, 0, 0, 0, 6, 0, 8, 0], self.game.getThreeByThreeArea(2,2))
        with self.assertRaises(IndexError):
            self.game.getThreeByThreeArea(7,0)


if __name__ == "__main__":
    unittest.main()