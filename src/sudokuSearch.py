from typing import Callable
from src.sudokuBoard import Board
import time

BACKTRACK_COUNTER = 0

# A recursive function to solve the Sudoku problem
def solveSudoku(sudokuBoard:Board, row:int, col:int, nodeExpandFunc: Callable[[Board],list[str]]):
    global BACKTRACK_COUNTER

    # base case: Reached nth column of the last row
    if row == (sudokuBoard.lexiconLength -1) and col == sudokuBoard.lexiconLength:
        return True

    # If past the last column of the row, then go to the next row
    if col == sudokuBoard.lexiconLength:
        row += 1
        col = 0

    # If cell is already occupied, then move forward
    if not sudokuBoard.isCellEmpty(row, col) :
        return solveSudoku(sudokuBoard, row, col + 1, nodeExpandFunc)

    choiceDomain = nodeExpandFunc(sudokuBoard)
    for num in choiceDomain:
        # If num can be placed at current position without violating Sudoku rules
        if sudokuBoard.validPlacement(row, col, str(num)) :
            sudokuBoard.fillCell(row, col, str(num))

            if solveSudoku(sudokuBoard, row, col + 1, nodeExpandFunc):
                return True
            
            # Backtrack
            sudokuBoard.fillCell(row, col, ' ')
            BACKTRACK_COUNTER += 1

    return False


def backtrackNodeExpansion(board:Board):
    return board.lexicon


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