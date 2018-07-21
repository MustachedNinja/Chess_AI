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
    if PLAYERS_TURN is None:
        initPlayersTurnsVar(current_state)
    MOVES.PLAYERS_TURN = PLAYERS_TURN
    new_state = CS.ChessState(current_state.board)

    new_state.whose_move = 1 - current_state.whose_move
    move_list = MOVES.generate_moves(PLAYERS_TURN, current_state.board)

    try:
        move = random.choice(moves_list)
        move_touple = (move[0], move[1])
        update_board((new_state, move_touple))
        return [move_touple, new_state]
    except:
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
