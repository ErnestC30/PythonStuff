"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

def isValidSudoku(board):
    return isRowsValid(board) and isColsValid(board) and isSquaresValid(board)

def isRowsValid(board):
    """Check if all rows in the board are correct."""
    for row in board:
        values = [i for i in row if i != "."]                           #Create list of values for each row.
        if len(values) != len(set(values)):                             #If there are duplicates, then len(set) will be smaller.
            return False
    return True

def isColsValid(board):
    """Check if all columns in the board are correct."""
    for col in zip(*board):                                             #Iterates over each column in board
        values = [i for i in col if i != "."]
        if len(values) != len(set(values)):
            return False
    return True    

def isSquaresValid(board):
    """Check if each 3x3 square in board is correct."""
    #Need to iterate over 3 x 3 for row and col
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):                                      
            values = []
            for i in range(0,3):                                        #Iterate between indexes 0-2, 3-5, 6-8 to check 3x3 squares
                for j in range(0,3):
                    if board[row+i][col+j] != ".":
                        values.append(board[row+i][col+j])

            if len(values) != len(set(values)):
                return False
    return True



#All Correct
board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

#Horizontally incorrect
board2 = [["5","3",".",".","7",".","8",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".","9","7","9"]]

#Vertically incorrect
board3 = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]


print(isValidSudoku(board))
print(isValidSudoku(board2))
print(isValidSudoku(board3))
