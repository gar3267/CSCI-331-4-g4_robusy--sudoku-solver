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
        # Getting file contents
        streamInput:str = stream.read()
        streamLines:list[str] = streamInput.split('\n')

        # Reading Lexicon
        lexiconInput:str = streamLines[0]
        self.lexicon = lexiconInput.split(',')
        lexiconLength:int = len(self.lexicon)

        # Creating board
        self.board = [[]]*lexiconLength
        for i in range(lexiconLength):
            boardInput:str = streamLines[i+1]
            self.board[i] = list(boardInput)
    

    def __str__(self):
        result:str = 'Lexicon:\n'+str(self.lexicon)+'\n\nBoard:'
        for row in self.board:
            result += '\n'+str(row)
        return result