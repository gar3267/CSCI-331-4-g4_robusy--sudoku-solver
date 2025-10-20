import io

class Board():
    board:list[list[str]]
    lexicon:list[str]


    def __init__(self, board:list[list[str]], lexicon:list[str]):
        """Basic initialization with directly passing in board and lexicon vairables"""
        self.board = board
        self.lexicon = lexicon


    def __init__(self, stream:io.TextIOWrapper):
        """
        Uses io stream to generate lexicon and board

        :param stream: stream to get input from
        """

        # Reading Lexicon
        lexiconInput:str = stream.read()
        self.lexicon = lexiconInput.split(',')
        lexiconLength:int = len(self.lexicon)

        # Creating board
        for i in range(lexiconLength):
            boardInput:str = stream.read()
            self.board[i] = list(boardInput)
    

    def __str__(self):
        print(self.lexicon)
        print(self.board)