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
    rs9 = bs.split("\n")
    rs8 = rs9[1:]  # eliminate the empty first item.
    for iy in range(8):
        rss = rs8[iy].split(' ')
        for jx in range(8):
            b[iy][jx] = INIT_TO_CODE[rss[jx]]
    return b



# ODDS = lowercase letters = Black (Player 1)
BOARD_PIECES_NUMBERS = {0:'-', 
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
