import src.sudokuRunner as sudokuRunner

def main():
    userInput:str = ''
    while True:
        print("Please enter what you want the program to do:\n\tt - Tests functionality of board\n\ttu - Tests functionality of board (with user)\n\ts - Runs search algorithms\n\tp - Runs pruning algorithm\n\tq - quits program")
        userInput = input().lower()
        match userInput:
            case 'q':
                break
            case 't':
                sudokuRunner.testBoard(withUser=False)
                continue
            case 'tu':
                sudokuRunner.testBoard(withUser=True)
                continue
            case 's':
                sudokuRunner.testSearchAlgorithms()
                continue
            case 'p':
                sudokuRunner.testPruningAlgorithms()
                continue
            case _:
                print("\nInput not within given list, try again.\n")
                continue
    

if __name__ == '__main__':
    main()