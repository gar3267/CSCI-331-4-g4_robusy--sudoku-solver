from src.sudokuBoard import Board
import time

BACKTRACK_COUNTER = 0

# A recursive function to solve the Sudoku problem
def solveSudokuBacktracking(sudokuBoard:Board, row, col):
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
        return solveSudokuBacktracking(sudokuBoard, row, col + 1)

    for num in sudokuBoard.lexicon:
        # If num can be placed at current position without violating Sudoku rules
        if sudokuBoard.validPlacement(row, col, str(num)) :
            sudokuBoard.fillCell(row, col, str(num))

            if solveSudokuBacktracking(sudokuBoard, row, col + 1):
                return True
            
            # Backtrack
            sudokuBoard.fillCell(row, col, ' ')
            BACKTRACK_COUNTER += 1

    return False


def backtrackSudoku(board:Board):
    global BACKTRACK_COUNTER
    BACKTRACK_COUNTER = 0

    solveSudokuBacktracking(board, 0, 0)

    return BACKTRACK_COUNTER


def backtrackSudokuTime(board:Board):
    global BACKTRACK_COUNTER
    BACKTRACK_COUNTER = 0
    start_time = time.perf_counter()

    result = solveSudokuBacktracking(board, 0, 0)

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