# CSCI-331-4-g4_robusy--sudoku-solver
Semester long group project in intro to AI which we can and should get done before the first half is done.

<br>

# Problem Description : 
Implement a solver for a Customized Sudoku Puzzle using constraint satisfaction techniques. The base rules of Sudoku apply that each row, column, and region must contain all digits without repetition. Implement and use two algorithms: (1) plain backtracking search and (2) backtracking enhanced with CSP methods such as forward checking or arc consistency

Also, report the difference in efficiency between the two algorithms and explain why the CSP-enhanced version performs better.

## Development Pipeline :
1 - Sudoku board creation
- Create a function that can create different sudoku puzzles, once given a specific lexicon
- Create a function that parses a file to read a specific sudoku puzzle
(print out the generated sudoku board to check if it does it correctly, and then try to solve it to see if it can be solved)

2 - Program Caller
- determines what functions we are using, what files we're reading
- can be through ptui, and argument where you read a file which basically has the ptui commands
(can use the same method to check if we did it correctly)

3 - Sudoku Solver
- Impliment both the backtracking DFS and the DFS with pruning enhancements
- maybe also do multithreading, but maybe not, I might have fun with multithreading I like multithreading :3
(can be checked easily with premade files)
