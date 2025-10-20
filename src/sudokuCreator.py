from .sudokuBoard import Board

def main():
    board1:Board
    with open('src/sudoku_boards/board1.txt','r') as file:
        board1 = Board(file)
    print(board1)


if __name__ == '__main__':
    main()