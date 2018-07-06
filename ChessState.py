"""
Defines a state in a game of chess
"""

def parse(initial_state_string):
    """Translates a nice looking string version of the
    # chess board into a 2D array with integers in order to be more functional.
    
    :param initial_state_string: intial state that is viusally pleasing
    :type initial_state_string: string
    :return: more functional board
    :rtype: 2D integer array
    """

    b = [[0, 0, 0, 0, 0, 0, 0, 0] for r in range(8)] #build 2D array
    rs9 = initial_state_string.split("\n")
    rs8 = rs9[1:]  # eliminate the empty first item.
    for iy in range(8):
        rss = rs8[iy].split(' ')
        for jx in range(8):
            b[iy][jx] = BOARD_PIECES_NUMBERS[rss[jx]]
    return b



# ODDS = lowercase letters = Black (Player 1)
BLACK = 1
WHITE = 0
BOARD_PIECES_NUMBERS = {'-':0, 
'p':1 ,'P':2, 
'h':3 ,'H':4 ,
'b':5, 'B':6, 
'r':7, 'R':8 , 
'q':9, 'Q':10, 
'k':11, 'K':12}

NUMBER_TO_PIECE = {0:'-', 
1:'p' ,2:'P', 
3: 'h' , 4: 'H' ,
5:'b', 6: 'B', 
7:'r', 8:'R' , 
9: 'q', 10:'Q', 
11:'k', 12:'K'}


INITIAL_BOARD = parse (
'''
r h b q k b h r
p p p p p p p p
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
P P P P P P P P
R K B Q K B H R
'''    
)


def who(piece):
    """
    Determines the piece's player or "color"
    :param piece: number of the piece (int)
    :return: the player of the piece (0 or 1)
    """
    return piece % 2




class ChessState:
    def __init__(self, old_board=INITIAL_BOARD, whose_move=WHITE):
        new_board = [r[:] for r in old_board]  # Deeply copy the board.
        self.board = new_board
        self.whose_move = whose_move

    def __repr__(self):  # Produce an ASCII display of the state.
        s = ''
        for r in range(8):
            for c in range(8):
                s += NUMBER_TO_PIECE[self.board[r][c]] + " "
            s += "\n"
        if self.whose_move == WHITE:
            s += "WHITE's move"
        else:
            s += "BLACK's move"
        s += "\n"

        return s

    def __eq__(self, other):
        if not (type(other) == type(self)):
            return False
        if self.whose_move != other.whose_move:
            return False
        try:
            b1 = self.board
            b2 = other.board
            for i in range(8):
                for j in range(8):
                    if b1[i][j] != b2[i][j]:
                        return False
            return True
        except Exception as e:
            return False


def test_starting_board():
    init_state = ChessState(INITIAL_BOARD, WHITE)
    print(init_state)


if __name__ == "__main__":
    test_starting_board()