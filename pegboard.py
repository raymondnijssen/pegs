class PegBoard():

    def __init__(self):
        self.matrix = self.getNewGame()
        self.moves = []


    def __str__(self):
        symbols = {0:'-', 1: 'O', 2: ' '}
        row_strs = []
        for row in self.matrix:
            row_sym = []
            for peg in row:
                row_sym.append(symbols[peg])
            row_strs.append(' '.join(row_sym))
        result = '\n'.join(row_strs)
        result += '\n'
        result += str(self.moves)
        result += '\n'
        result += 'moves: {}, pegs: {}'.format(len(self.moves), self.getNumPegs())
        return result


    def getNewGame(self):
        result = [[2, 2, 1, 1, 1, 2, 2],
            [2, 2, 1, 1, 1, 2, 2],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [2, 2, 1, 1, 1, 2, 2],
            [2, 2, 1, 1, 1, 2, 2]
        ]
        return result

    def getAllMoves(self):
        result = []
        for row_id in range(0,7):
            for col_id in range(0,7):
                moves_for_peg = self.getMovesForPeg(row_id, col_id)
                result += moves_for_peg
                #print(row_id, col_id, len(moves_for_peg))
        return result


    def getMovesForPeg(self, x, y):
        result = []
        if self.isValidMove(x, y, x, y+2): #north
            result.append([x, y, x, y+2])
        if self.isValidMove(x, y, x+2, y): #east
            result.append([x, y, x+2, y])
        if self.isValidMove(x, y, x, y-2): #south
            result.append([x, y, x, y-2])
        if self.isValidMove(x, y, x-2, y): #west
            result.append([x, y, x-2, y])
        return result


    def isValidMove(self, x0, y0, x2, y2):
        ids = [0,1,2,3,4,5,6]
        if not (x0 in ids and y0 in ids and x2 in ids and y2 in ids):
            return False
        p0 = self.matrix[x0][y0]
        p1 = self.matrix[ round( (x0+x2)/2 ) ][ round( (y0+y2)/2 ) ]
        p2 = self.matrix[x2][y2]
        return (p0 == 1 and p1 == 1 and p2 == 0)

    def doMove(self, x0, y0, x2, y2):
        self.matrix[x0][y0] = 0
        self.matrix[ round( (x0+x2)/2 ) ][ round( (y0+y2)/2 ) ] = 0
        self.matrix[x2][y2] = 1
        self.moves.append([x0, y0, x2, y2])

    def getNumPegs(self):
        return 32 - len(self.moves)
        result = 0
        for row in self.matrix:
            for peg in row:
                if peg == 1:
                    result += 1
        return result
