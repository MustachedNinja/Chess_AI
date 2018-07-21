"""
A Chess playing agent which uses a smart heuristic and Zobrist hashing to determine the next move
Uses information gathered from the game to comment on the game to its opponent
"""

import random
import ChessState as CS
import GenerateMoves as MOVES
PLAYERS_TURN = None


def initPlayersTurnsVar(curr_state):
    global PLAYERS_TURN

    if curr_state.whose_move == 0:
        PLAYERS_TURN = 0
    else:
        PLAYERS_TURN = 1


def make_move(current_state, current_remark, time_limit):
    print("Trying to move player 1")
    if PLAYERS_TURN is None:
        initPlayersTurnsVar(current_state)
    MOVES.PLAYERS_TURN = PLAYERS_TURN
    new_state = CS.ChessState(current_state.board)

    new_state.whose_move = 1 - current_state.whose_move
    move_list = MOVES.generate_moves(PLAYERS_TURN, current_state.board)

    try:
        print("Generating a move")
        move = random.choice(moves_list)
        move_touple = (move[0], move[1])
        update_board((new_state, move_touple))
        return [move_touple, new_state]
    except:
        print("Movement failed")
        pass


def update_board(new_state, move):
    old_pos = move[0]
    new_pos = move[1]
    piece = new_state.board[old_pos[0]][old_pos[1]]

    new_state.board[old_pos[0]][old_pos[1]] = 0
    new_state.board[old_pos[0]][new_pos[1]] = piece


def prepare():
    board_value = EVAL.eval_board(board, player)
    move_list = MOVES.generate_moves(player, board)
    board_value += len(move_list)
    pass


def dumb_heuristic(board):
    count = 0
    for row in board:
        for col in board[row]:
            piece = board[row][col]
            if piece != 0:
                if piece % 2 != PLAYERS_TURN:
                    count -= piece
                elif piece % 2 == PLAYERS_TURN:
                    count += piece
    return count
<<<<<<< HEAD


def generate_evaluate_moves(board):
    """
    Used ONLY in the prepare function, not to be used in make_move
    When precomputing, this function evaluates the heuristic value of the current board
    as well as all possible moves from the current board
    param board: the current board as a 2D array of ints
    return: an array of the format [heuristic_value, list_of_moves]
    """
    import EvaluatePiece as EVAL

    move_list = []
    bishop_count = 0
    board_count = 0

    for row in board:
        for col in board[row]:
            if CS.who(board[row][col]) == PLAYERS_TURN:

                piece_pos = (row, col)
                piece = board[piece_pos[0]][piece_pos[1]]
                piece -= (piece % 2)
                piece_list = []

                if piece == MOVES.PAWN:
                    MOVES.generate_pawn(piece_pos, board, piece_list, PLAYERS_TURN)
                    piece_val = EVAL.eval_pawn(piece_pos, board, PLAYERS_TURN)
                if piece == MOVES.ROOK:
                    MOVES.generate_rook(piece_pos, board, piece_list, PLAYERS_TURN)
                    piece_val = EVAL.eval_rook(piece_pos, board, PLAYERS_TURN)
                if piece == MOVES.KNIGHT:
                    MOVES.generate_knight(piece_pos, board, piece_list, PLAYERS_TURN)
                    piece_val = EVAL.eval_knight(piece_pos, board, PLAYERS_TURN)
                if piece == MOVES.BISHOP:
                    bishop_count = bishop_count + 1
                    MOVES.generate_bishop(piece_pos, board, piece_list, PLAYERS_TURN)
                    piece_val = EVAL.eval_bishop(piece_pos, board, PLAYERS_TURN)
                if piece == MOVES.QUEEN:
                    MOVES.generate_queen(piece_pos, board, piece_list, PLAYERS_TURN)
                    piece_val = EVAL.eval_queen(piece_pos, board, PLAYERS_TURN)
                if piece == MOVES.KING:
                    MOVES.generate_king(piece_pos, board, piece_list, PLAYERS_TURN)
                    piece_val = EVAL.eval_king(piece_pos, board, PLAYERS_TURN)
                piece_val += len(piece_list)
                board_count += piece_val
    if bishop_count is 2:
        board_count += 10

    return_list = [board_count, move_list]
    return return_list
=======
>>>>>>> Kostya_branch
