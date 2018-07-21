"""
Defines a state in a game of chess
"""

def who(piece):
    """
    Determines the piece's player or "color"
    :param piece: number of the piece (int)
    :return: the player of the piece (-1 for empty, 0 or 1)
    """
    if piece is not 0:
        return piece % 2
    else:
        return -1
