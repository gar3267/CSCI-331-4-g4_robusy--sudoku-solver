from .sudokuBoard import Board
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
    badValidBoards:list[Board] = getBoardsFromFolder('src/sudoku_boards/bad_boards')
    for board in badValidBoards:
        print('\n'+str(board))
        validity = board.validate()
        print(validity)
        if validity is None:
            print('============================\nVALIDITY SHOULD HAVE FAILED\n============================')

    # Testing user input
    if withUser:
        userBoard:Board = Board()
        print(userBoard)
        print(userBoard.validate())


def getUserBoard():
    """Uses board's init to get a board from user input"""
    return Board()


def getBoardsFromFolder(path:str = 'src/sudoku_boards'):
    """Gets all the boards pathin sudoku_boards folder then returns them as list"""
    dir_list = os.listdir(path)
    result:list[Board] = []

    # If it blows up, that tells you that you did the file wrong
    for filename in dir_list:
        fileBoard:Board
        if filename[-4:] == '.sud':
            with open(path+'/'+filename,'r') as file:
                fileBoard = Board(file=file)
                result.append(fileBoard)
    
    return result


def testSearchAlgorithms():
    pass