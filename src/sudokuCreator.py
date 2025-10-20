from .sudokuBoard import Board

def testBoard():
    board0:Board = Board(lexicon=['a','b','c'],board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']])
    print(board0)
    print(board0.validate())

    board1:Board
    with open('src/sudoku_boards/board1.txt','r') as file:
        board1 = Board(file=file)
    print(board1)
    print(board1.validate())
    
    answer1:Board
    with open('src/sudoku_boards/answers/answer1.txt','r') as file:
        answer1 = Board(file=file)
    print('\n'+str(answer1))
    print(answer1.validate())
    
    # Testing validity
    rowValid:Board
    with open('src/sudoku_boards/badBoards/rowValidFail.txt','r') as file:
        rowValid = Board(file=file)
    print('\n'+str(rowValid))
    print(rowValid.validate())

    colValid:Board
    with open('src/sudoku_boards/badBoards/colValidFail.txt','r') as file:
        colValid = Board(file=file)
    print('\n'+str(colValid))
    print(colValid.validate())

    squareValid:Board
    with open('src/sudoku_boards/badBoards/squareValidFail.txt','r') as file:
        squareValid = Board(file=file)
    print('\n'+str(squareValid))
    print(squareValid.validate())

    # Testing user input
    userBoard:Board
    userBoard = Board()
    print(userBoard)
    print(userBoard.validate())