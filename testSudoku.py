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

    def testIsSectionComplete(self):
        self.assertTrue(self.game.isSectionComplete([4, 2, 3, 1, 5, 6, 7, 8, 9]))
        self.assertFalse(self.game.isSectionComplete([2, 2, 3, 1, 5, 6, 7, 8, 9]))

        with self.assertRaises(IndexError):
            self.game.isSectionComplete([0, 1, 2, 3])

    def testGetRow(self):
        self.assertEquals([8, 0, 0, 0, 6, 0, 0, 0, 3], self.game.getRow(3))
        self.assertEquals([0, 0, 0, 4, 1, 9, 0, 0, 5], self.game.getRow(7))

    def testGetColumn(self):
        self.assertEqual([0, 0, 8, 0, 0, 0, 0, 0, 0], self.game.getColumn(2))

    def testGetSubgrid(self):
        self.assertEquals([0, 7, 0, 1, 9, 5, 0, 0, 0], self.game.getSubgrid(1))
        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 6, 0], self.game.getSubgrid(2))
        self.assertEqual([8 ,0 ,0 ,4 ,0 ,0 ,7 ,0 ,0], self.game.getSubgrid(3))
        self.assertEqual([0 ,6 ,0 ,8 ,0 ,3 ,0 ,2 ,0], self.game.getSubgrid(4))
        self.assertEqual([0 ,0 ,0 ,4 ,1 ,9 ,0 ,8 ,0], self.game.getSubgrid(7))
        with self.assertRaises(IndexError):
            self.game.getSubgrid(-1)
            self.game.getSubgrid(9)

    
    def testGetThreeByThreeArea(self):
        self.assertEqual([5, 3, 0, 6, 0, 0, 0, 9, 8], self.game.getThreeByThreeArea(0,0))
        self.assertEqual([2, 8, 0, 0, 0, 5, 0, 7, 9], self.game.getThreeByThreeArea(6,6))
        self.assertEqual([7, 0, 0, 9, 5, 0, 0, 0, 0], self.game.getThreeByThreeArea(4,0))
        with self.assertRaises(IndexError): # tests exception handling
            self.game.getThreeByThreeArea(-1,0)
            self.game.getThreeByThreeArea(0,-1)
            self.game.getThreeByThreeArea(7,0)
            self.game.getThreeByThreeArea(0,7)
    
    


            


if __name__ == "__main__":
    unittest.main()