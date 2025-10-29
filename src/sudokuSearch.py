from typing import Callable
from src.sudokuBoard import Board
import time

BACKTRACK_COUNTER = 0

# A recursive function to solve the Sudoku problem
def solveSudoku(sudokuBoard:Board, row:int, col:int, nodeExpandFunc:Callable[[Board],list[str]], nodeExpArgs:list = None):
    global BACKTRACK_COUNTER

    # base case: Reached nth column of the last row
    if row == (sudokuBoard.lexiconLength -1) and col == sudokuBoard.lexiconLength:
        return sudokuBoard.validate()==None # Returning board validity

    # If past the last column of the row, then go to the next row
    if col == sudokuBoard.lexiconLength:
        row += 1
        col = 0

    # If cell is already occupied, then move forward
    if not sudokuBoard.isCellEmpty(row, col) :
        return solveSudoku(sudokuBoard, row, col + 1, nodeExpandFunc)

    result = nodeExpandFunc(sudokuBoard, row, col, nodeExpArgs)
    choiceDomain = result[0]
    nodeExpArgs = result[1]
    for num in choiceDomain:
        # Filling cell with first num in domain
        sudokuBoard.fillCell(row, col, str(num))

        if solveSudoku(sudokuBoard, row, col + 1, nodeExpandFunc):
            return sudokuBoard.validate()==None # Returning board validity
            
        # Backtrack
        sudokuBoard.fillCell(row, col, ' ')
        BACKTRACK_COUNTER += 1

    return False


def backtrackNodeExpansion(board:Board, row=None, col=None, nodeExpArgs=None):
    return (board.lexicon,None)


def basicPrunedNodeExpansion(board:Board, row:int, col:int, nodeExpArgs=None):
    choices = board.lexicon
    result = []

    for choice in choices:
        if board.validPlacement(row,col,choice):
            result.append(choice)
        
    return (result,None)


def backtrackSudoku(board:Board):
    global BACKTRACK_COUNTER
    BACKTRACK_COUNTER = 0

    solveSudoku(board, 0, 0, backtrackNodeExpansion)

    return BACKTRACK_COUNTER


def backtrackSudokuTime(board:Board):
    global BACKTRACK_COUNTER
    BACKTRACK_COUNTER = 0
    start_time = time.perf_counter()

    result = solveSudoku(board, 0, 0, backtrackNodeExpansion)

    end_time = time.perf_counter()

    return BACKTRACK_COUNTER, end_time - start_time


def backtrackPrunedSudoku(board:Board):
    global BACKTRACK_COUNTER
    BACKTRACK_COUNTER = 0

    solveSudoku(board, 0, 0, basicPrunedNodeExpansion)

    return BACKTRACK_COUNTER


def backtrackPrunedSudokuTime(board:Board):
    global BACKTRACK_COUNTER
    BACKTRACK_COUNTER = 0
    start_time = time.perf_counter()

    result = solveSudoku(board, 0, 0, basicPrunedNodeExpansion)

    end_time = time.perf_counter()

    return BACKTRACK_COUNTER, end_time - start_time


if __name__ == "__main__":
    
    board1:Board
    with open('src/sudoku_boards/board1.sud','r') as file:
        board1 = Board(file=file)
    print(board1)

    print('\nSolving...\n')

    count, seconds = backtrackSudokuTime(board1)
    print('\nSolved in ' + str(seconds) + ' seconds with ' + str(count) + ' backtracking steps\n')
    print(board1)

    answer1:Board
    with open('src/sudoku_boards/answers/answer1.sud','r') as file:
        answer1 = Board(file=file)
    print('\n'+str(board1.equals(answer1)))