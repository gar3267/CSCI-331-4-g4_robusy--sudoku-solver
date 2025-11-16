from typing import Callable
from src.sudokuBoard import Board
import time
import copy

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

        if nodeExpandFunc == forwardCheckingNodeExpansion:
            # Perform forward checking before recursing
            new_domains = forwardCheckDomains(sudokuBoard, row, col, str(num), nodeExpArgs)
            if new_domains is None:
                sudokuBoard.fillCell(row, col, ' ')
                BACKTRACK_COUNTER += 1
                continue  # Domain wipeout, backtrack early

            if solveSudoku(sudokuBoard, row, col + 1, nodeExpandFunc, new_domains):
                return sudokuBoard.validate() == None

        else:
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


def initializeDomains(board: Board):
    """Initialize domains for all cells (possible values each cell can take)."""
    domains = {}
    for i in range(board.lexiconLength):
        for j in range(board.lexiconLength):
            if board.isCellEmpty(i, j):
                domains[(i, j)] = [
                    val for val in board.lexicon if board.validPlacement(i, j, val)
                ]
            else:
                domains[(i, j)] = [board.board[i][j]]
    return domains


def forwardCheckDomains(board: Board, row: int, col: int, val: str, domains: dict):
    """
    Perform forward checking:
    remove `val` from the domain of all neighbors (same row, column, box).
    Return a new domains dict (copied), or None if a domain becomes empty.
    """
    new_domains = copy.deepcopy(domains)
    new_domains[(row, col)] = [val]  # Fixed domain

    size = board.lexiconLength
    box_size = int(size ** 0.5)

    # Compute all neighbor coordinates
    neighbors = set()
    for i in range(size):
        neighbors.add((row, i))  # Row
        neighbors.add((i, col))  # Col
    start_row = (row // box_size) * box_size
    start_col = (col // box_size) * box_size
    for i in range(start_row, start_row + box_size):
        for j in range(start_col, start_col + box_size):
            neighbors.add((i, j))

    neighbors.discard((row, col))

    for (r, c) in neighbors:
        if board.isCellEmpty(r, c):
            if val in new_domains[(r, c)]:
                new_domains[(r, c)].remove(val)
                if len(new_domains[(r, c)]) == 0:
                    return None  # Domain wiped out → fail early

    return new_domains


def forwardCheckingNodeExpansion(board: Board, row: int, col: int, nodeExpArgs=None):
    """
    Forward checking node expansion.
    nodeExpArgs: current domains (dict)
    """
    if nodeExpArgs is None:
        nodeExpArgs = initializeDomains(board)

    # Get possible values for this cell from its domain
    choices = nodeExpArgs[(row, col)]
    return (choices, nodeExpArgs)


def forwardCheckingSudoku(board: Board):
    global BACKTRACK_COUNTER
    BACKTRACK_COUNTER = 0

    domains = initializeDomains(board)
    solveSudoku(board, 0, 0, forwardCheckingNodeExpansion, domains)

    return BACKTRACK_COUNTER


def forwardCheckingSudokuTime(board: Board):
    global BACKTRACK_COUNTER
    BACKTRACK_COUNTER = 0
    start_time = time.perf_counter()

    domains = initializeDomains(board)
    solveSudoku(board, 0, 0, forwardCheckingNodeExpansion, domains)

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