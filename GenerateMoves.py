"""
Generates all the possible moves for a given state in a game of chess
"""

import ChessState as CS

"""
board accesses --> board[row][col]
a move is defined as a list of tuples [(old_pos),(new_pos)]
"""

"""
A possible idea is to make the pieces as classes (general class "Piece" and inherited classes for individual pieces)
and then have the individual classes have the methods that generate moves"""



def generate_moves(player, board):
    """
    Generates all the moves for a given |board| and current |player|
    :param player: the current player making the move (either 0 or 1)
    :param board: current configuration of the board
    :return: a list of all possible moves
    """
    """
    move_list = []
    for each row
        for each col
            if CS.who(board[row][col]) == current_player
            generate all the moves for that piece
            find_moves_for_piece((row, col), board)
            ->  Have a helper method which is a giant list of if statements
            ->  That helper method calls other helper methods to generate a list
    
    return move_list
    """

def find_moves_for_piece(piece_pos, board):
    """
    Finds all the moves possible for a given piece
    :param piece_pos: The position of the piece to be inspected represented by a tuple (row, col)
    :param board: current configuration of the board
    :return: a list of all moves possible by that piece
    """
    """
    return_list = []
    if pawn:
        generate_pawn(piece_pos, board, return_list)
    if rook:
        generate_rook(piece_pos, board, return_list)
    if knight:
        generate_knight(piece_pos, board, return_list)
    if bishop:
        generate_bishop(piece_pos, board, return_list)
    if queen:
        generate_queen(piece_pos, board, return_list)
    if king:
        generate_king(piece_pos, board, return_list)
    
    return return_list"""

def generate_pawn(pos, board, list):
    """
    Generates all possible moves for a pawn at the given position
    :param pos: position of the pawn represented by a tuple (row, col)
    :param board: current state of the board
    :param list: list of possible moves which will be added to
    :return: none
    """
    """
    Pawns can move one ahead, or two ahead if they are in their initial position (check official rules)
    They can capture by moving to the top left or top right   
    # non-lethal moves
    if there is space infront of the pawn:
        add a move
    if the pawn is in the initial position:
        if there is space two tiles ahead:
            add pos[0] + 1, pos[1] + 1
    
    # lethal moves
    if there is an enemy piece to the top left:
        add move
    if there is an enemy piece to the top right:
        add move
    (check if it can kill backwards (bottom left and bottom right)
    """

def generate_rook(pos, board, list):
    """
    Generates all possible moves for a rook at the given pos
    :param pos: position of the pawn represented by a tuple (row, col)
    :param board: current state of the board
    :param list: list of possible moves which will be added to
    :return: none
    """
    """
    Rooks can move forward and backwards as much as they want, and can kill the same way
    Also, if the king and rook have not moved this game, they can do a fancy position switch (don't add this yet)
    # non-lethal moves
    if space above rook i
    """
