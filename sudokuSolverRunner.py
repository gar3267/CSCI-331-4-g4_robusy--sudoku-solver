import src.sudokuRunner as sudokuRunner

def main():
    sudokuRunner.testBoard(withUser=True)
    sudokuRunner.getBoardsFromFolder('src/sudoku_boards/bad_boards')
    

if __name__ == '__main__':
    main()