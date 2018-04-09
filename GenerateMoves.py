"""
Generates all the possible moves for a given state in a game of chess
"""

import ChessState as CS

"""
board accesses --> board[row][col]
a move is defined as a list of tuples [(old_pos),(new_pos)]
"""

# Weights of all the pieces (also used for identification)
PAWN = 2
ROOK = 10
KNIGHT = 8
BISHOP = 8
QUEEN = 12
KING = 16


def generate_moves(player, board):
    """
    Generates all the moves for a given |board| and current |player|
    :param player: the current player making the move (either 0 or 1)
    :param board: current configuration of the board
    :return: a list of all possible moves
    """
    move_list = []
    for row in board:
        for col in board[row]:
            if CS.who(board[row][col]) == player:
                piece_list = find_moves_for_piece((row, col), board)
                move_list.append(piece_list)
    
    return move_list


def find_moves_for_piece(piece_pos, board):
    """
    Finds all the moves possible for a given piece
    :param piece_pos: The position of the piece to be inspected represented by a tuple (row, col)
    :param board: current configuration of the board
    :return: a list of all moves possible by that piece
    """
    return_list = []
    piece = board[piece_pos[0]][piece_pos[1]]
    piece -= (piece % 2)
    if piece == PAWN:
        generate_pawn(piece_pos, board, return_list)
    if piece == ROOK:
        generate_rook(piece_pos, board, return_list)
    if piece == KNIGHT:
        generate_knight(piece_pos, board, return_list)
    if piece == BISHOP:
        generate_bishop(piece_pos, board, return_list)
    if piece == QUEEN:
        generate_queen(piece_pos, board, return_list)
    if piece == KING:
        generate_king(piece_pos, board, return_list)
    
    return return_list


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
