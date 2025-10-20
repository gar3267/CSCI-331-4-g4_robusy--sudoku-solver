import io, math

class Board():
    board:list[list[str]]
    lexicon:list[str]
    lexiconLength:int


    def __init__(self, board:list[list[str]], lexicon:list[str]):
        """Basic initialization with directly passing in board and lexicon vairables"""
        self.board = board
        self.lexicon = lexicon


    def __init__(self, file:io.TextIOWrapper):
        """
        Uses file to generate lexicon and board

        :param file: file to get input from
        """
        # Getting file contents
        fileInput:str = file.read()
        fileLines:list[str] = fileInput.split('\n')

        # Reading Lexicon
        lexiconInput:str = fileLines[0]
        self.lexicon = lexiconInput.split(',')
        self.lexiconLength = len(self.lexicon)

        # Creating board
        self.board = [[]]*self.lexiconLength
        for i in range(self.lexiconLength):
            boardInput:str = fileLines[i+1]
            self.board[i] = list(boardInput)
    

    def validate(self):
        """
        Validates if the board is a solution
        
        :return: On success None, on failure string with reason
        """
        # Checking for spaces, and row validity
        for row in self.board:
            rowDict:dict[str,None] = {}
            for entry in row:
                if entry == ' ':
                    return 'Entry validity failure.'
                if entry in rowDict:
                    return 'Row validity failure.'
                rowDict[entry] = None

        # Checking for col validity
        for j in range(self.lexiconLength):
            colDict:dict[str,None] = {}
            for i in range(self.lexiconLength):
                entry = self.board[i][j]
                if entry in colDict:
                    return 'Column validity failure.'
                colDict[entry] = None
        
        # Checking for square validity
        squareDim:int = int(math.sqrt(self.lexiconLength))
        for outerI in range(squareDim):
            for outerJ in range(squareDim):
                squareDict:dict[str,None] = {}
                for i in range(outerI*squareDim,(outerI+1)*squareDim):
                    for j in range(outerJ*squareDim,(outerJ+1)*squareDim):
                        entry = self.board[i][j]
                        if entry in squareDict:
                            return 'Square validity failure.'
                        squareDict[entry] = None
        
        # Found no issues so return None
        return None
    

    def __str__(self):
        result:str = 'Lexicon:\n'+str(self.lexicon)+'\n\nBoard:'
        for row in self.board:
            result += '\n'+str(row)
        return result