# sudokuSolver

## Sudoku Game Implementation

The class sudokuGame, defined in sudoku.py, provides everything the backtracking algorithm needs to solve a soduku puzzle. 

sudokuGame has getters for the puzzle's rows, columns, and subgrids. All of which return arrays with their values.

Since the getter functions return an array, the function *FILLNAMEHERE()* traverses the array and returns true if the array contains all digits 1 through 9

**isSectionComplete()**

Exception Handling: throws IndexError if input array is not a size of 9
- Since isSectionComplete() only checks arrays from the getter functions, there is no reason for them to be != 9

Uses a Set to account for every unique digit added
- Every element in a set is unique, so adding every element of the array to the set will signify if there are duplicate elements

if len(set) == 9, it returns True, since that means every element of the given array is unique and is a value 1-9. It will return False otherwise.

