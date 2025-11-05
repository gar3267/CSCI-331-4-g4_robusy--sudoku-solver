import src.sudokuSearch as sudokuSearch
from src.sudokuBoard import Board
import os

def testBoard(withUser=False):
    board0:Board = Board(lexicon=['a','b','c'],board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']])
    print(board0)
    validity:str = board0.validate()
    print(validity)
    if validity is None:
        print('============================\nVALIDITY SHOULD HAVE FAILED\n============================')

    board1:Board
    with open('src/sudoku_boards/board1.sud','r') as file:
        board1 = Board(file=file)
    print(board1)
    validity = board1.validate()
    print(validity)
    if validity is None:
        print('============================\nVALIDITY SHOULD HAVE FAILED\n============================')
    
    answer1:Board
    with open('src/sudoku_boards/answers/answer1.sud','r') as file:
        answer1 = Board(file=file)
    print('\n'+str(answer1))
    validity = answer1.validate()
    print(validity)
    if validity is not None:
        print("==============================\nVALIDITY SHOULDN'T HAVE FAILED\n==============================")
    
    # Testing validity
    badValidBoards:list[tuple[Board,str]] = getBoardsFromFolder('src/sudoku_boards/bad_boards')
    for board in badValidBoards:
        print('\n'+str(board[1])+'\n'+str(board[0]))
        validity = board[0].validate()
        print(validity)
        if validity is None:
            print('============================\nVALIDITY SHOULD HAVE FAILED\n============================')

    # Testing user input
    if withUser:
        userBoard:Board = Board()
        print(userBoard)
        print(userBoard.validate())
    
    # Adding extra enter
    print()


def getUserBoard():
    """Uses board's init to get a board from user input"""
    return Board()


def getBoardsFromFolder(path:str = 'src/sudoku_boards'):
    """Gets all the boards pathin sudoku_boards folder then returns them as list"""
    dir_list = os.listdir(path)
    result:list[tuple[Board,str]] = []

    # If it blows up, that tells you that you did the file wrong
    for filename in dir_list:
        fileBoard:Board
        if filename[-4:] == '.sud':
            with open(path+'/'+filename,'r') as file:
                fileBoard = Board(file=file)
                result.append((fileBoard,filename))
    
    return result


def testSearchAlgorithms():
    # Testing with pruned
    print('Testing with pruned node expansions.')
    testBoards = getBoardsFromFolder()
    for board in testBoards:
        print('\nTesting '+str(board[1]))
        count, seconds = sudokuSearch.backtrackPrunedSudokuTime(board[0])
        print('\nSolved in ' + str(seconds) + ' seconds with ' + str(count) + ' backtracking steps\n')

    # Testing with backtrack
    print('Testing with basic backtracking algorithm.')
    testBoards = getBoardsFromFolder()
    for board in testBoards:
        print('\nTesting '+str(board[1]))
        count, seconds = sudokuSearch.backtrackSudokuTime(board[0])
        print('\nSolved in ' + str(seconds) + ' seconds with ' + str(count) + ' backtracking steps\n')