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
    

    def __init__(self):
        """No parameters so ask for terminal user input"""
        # Getting Lexicon
        theUserStupid:bool = True
        lexiconInput:list
        while theUserStupid:
            lexiconInput = input("Enter the lexicon (ex: 'a,1,2,b,c,d,D'):\n").split(',')
            
            # Checking if each character is a character and none are spaces
            theUserIsVeryStupid:bool = False
            for entry in lexiconInput:
                if len(entry) != 1:
                    print("Lexicon can only consist of entries of length 1: "+entry)
                    theUserIsVeryStupid = True
                    break
                if entry == ' ':
                    print("Spaces cannot be part of the lexicon, please try again.")
                    theUserIsVeryStupid = True
                    break
            if theUserIsVeryStupid:
                continue

            # Checking size of lexicon is a squareroot
            lexLengthSqrt = math.sqrt(len(lexiconInput))
            if float(int(lexLengthSqrt)) != lexLengthSqrt:
                print("Lexicon length is not a perfect square, please try again.")
                continue
            theUserStupid = False
        self.lexicon = lexiconInput
        self.lexiconLength = len(self.lexicon)

        # Creating board
        self.board = [[]]*self.lexiconLength
        lexiconDomain:list[str] = self.lexicon + [' ']
        for i in range(self.lexiconLength):
            theUserStupid = True
            boardInput:list

            # Getting input
            while theUserStupid:
                boardInput = list(input("Enter the next row (ex: 'a b '):\n"))

                # Checking for row length
                if len(boardInput) != self.lexiconLength:
                    print("Row isn't equal to the size of the row length: "+str(self.lexiconLength))
                    continue

                # Checking if within lexicon
                theUserIsVeryStupid:bool = False
                for entry in boardInput:
                    if entry not in lexiconDomain:
                        print("You used a value outside of the lexicon: "+entry)
                        theUserIsVeryStupid = True
                if theUserIsVeryStupid:
                    continue

                # We got good input so leave
                theUserStupid = False
            
            self.board[i] = boardInput
    

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