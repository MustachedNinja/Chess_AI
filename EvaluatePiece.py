"""
Used to evaluate the static value of a piece at a given position on the board
"""

import ChessState as CS
import GenerateMoves as MOVES

PLAYER = None


pawn_weights =   
[[ 0,  0,  0,  0,  0,  0,  0,  0],
 [50, 50, 50, 50, 50, 50, 50, 50],
 [10, 10, 20, 30, 30, 20, 10, 10],
 [ 5,  5, 10, 27, 27, 10,  5,  5],
 [ 0,  0,  0, 25, 25,  0,  0,  0],
 [ 5, -5,-10,  0,  0,-10, -5,  5],
 [ 5, 10, 10,-25,-25, 10, 10,  5],
 [ 0,  0,  0,  0,  0,  0,  0,  0]]

knight_weights =
[[-50,-40,-30,-30,-30,-30,-40,-50],
 [-40,-20,  0,  0,  0,  0,-20,-40],
 [-30,  0, 10, 15, 15, 10,  0,-30],
 [-30,  5, 15, 20, 20, 15,  5,-30],
 [-30,  0, 15, 20, 20, 15,  0,-30],
 [-30,  5, 10, 15, 15, 10,  5,-30],
 [-40,-20,  0,  5,  5,  0,-20,-40],
 [-50,-40,-20,-30,-30,-20,-40,-50]]

bishop_weights = 
[[-20,-10,-10,-10,-10,-10,-10,-20],
 [-10,  0,  0,  0,  0,  0,  0,-10],
 [-10,  0,  5, 10, 10,  5,  0,-10],
 [-10,  5,  5, 10, 10,  5,  5,-10],
 [-10,  0, 10, 10, 10, 10,  0,-10],
 [-10, 10, 10, 10, 10, 10, 10,-10],
 [-10,  5,  0,  0,  0,  0,  5,-10],
 [-20,-10,-40,-10,-10,-40,-10,-20]]

king_table = 
[[-30,-40,-40,-50,-50,-40,-40,-30],
 [-30,-40,-40,-50,-50,-40,-40,-30],
 [-30,-40,-40,-50,-50,-40,-40,-30],
 [-30,-40,-40,-50,-50,-40,-40,-30],
 [-20,-30,-30,-40,-40,-30,-30,-20],
 [-10,-20,-20,-20,-20,-20,-20,-10], 
 [ 20, 20,  0,  0,  0,  0, 20, 20],
 [ 20, 30, 10,  0,  0, 10, 30, 20]]


def eval_piece(pos, board):
	"""
	Calculates a score based on whether a piece is attacked or defended. 
	Promotes being defended with no attackers.
	param pos: position of piece on board as a tuple of ints
	param board: current board configuration as a 2D array of ints
	return: the score depending on whether the piece is defended or attacked
	"""
	score = 0
	defended_val = is_defended(pos, board)
	attacked_val = is_attacked(pos, board)
	if defended_val < abs(attacked_val):
		score += 2 * attacked_val
	else:
		score += (defended_val + attacked_val)
	return score


def eval_pawn(pos, board, player):
	global PLAYER
	PLAYER = player
	score = CS.PAWN
	score += pawn_weights[pos[0]][pos[1]]
	score += eval_piece(pos, board)
	return score


def eval_rook(pos, board, player):
	global PLAYER
	PLAYER = player
	score = CS.ROOK
	score += eval_piece(pos, board)
	return score


def eval_knight(pos, board, player):
	global PLAYER
	PLAYER = player
	score = CS.KNIGHT
	score += knight_weights[pos[0]][pos[1]]
	score += eval_piece(pos, board)
	return score

def eval_bishop(pos, board, player):
	global PLAYER
	PLAYER = player
	score = CS.BISHOP
	score += bishop_weights[pos[0]][pos[1]]
	score += eval_piece(pos, board)
	return score


def eval_queen(pos, board, player):
	global PLAYER
	PLAYER = player
	score = CS.QUEEN
	score += eval_piece(pos, board)
	return score


def eval_king(pos, board, player):
	global PLAYER
	PLAYER = player
	score = CS.KING
	score += knight_weights[pos[0]][pos[1]]
	score += eval_piece(pos, board)
	return score


def is_defended(pos, board):
	"""
	Determines if a piece is defended or not and returns a value that is larger 
	if the defending piece is weaker than the defended piece
	param pos: position of piece as a tuple of ints
	param board: current board state as a 2D array of ints
	param player: current player as an int of 0 or 1
	return: int the determines whether a piece is defended
	"""
	# first two can be either pawns, king or queen, next 6 are king, next 8 are knights
	relative_pos = [(-1, -1), (-1, 1), (1, 0), (1, 1), (1, -1), (-1, 0), (0, 1), (0, -1)]
	knight_pos = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
	
	total_list = []
	total_list.append(relative_pos)
	total_list.append(knight_pos)
	queen_check(pos, board, total_list, PLAYER)

	piece = board[pos[0]][pos[1]] - PLAYER

	for piece_pos in total_list:
		if CS.legal_move(piece_pos):

			defend_piece = board[piece_pos[0]][piece_pos[1]]
			defend_piece = defend_piece - defend_piece % 2

			if defend_piece is not 0 and defend_piece % 2 is PLAYER:
				if piece > defend_piece:
					return 15
				elif piece < defend_piece:
					return 7
				else
					return 0


def is_attacked(pos, board):
	"""
	Determines if a piece is attacked and returns a value that is larger
	if the attacking piece is weaker than the attacked piece
	param pos: position of piece as a tuple of ints
	param board: current board state as a 2D array of ints
	param player: current player as an int of 0 or 1
	return: int the determines whether a piece is attacked
	"""
	relative_pos = [(-1, -1), (-1, 1), (1, 0), (1, 1), (1, -1), (-1, 0), (0, 1), (0, -1)]
	knight_pos = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
	
	total_list = []
	total_list.append(relative_pos)
	total_list.append(knight_pos)

	if PLAYER is 1:
		enemy = 0
	else:
		enemy = 1
	
	queen_check(pos, board, total_list, enemy)

	piece = board[pos[0]][pos[1]] - PLAYER

	for piece_pos in total_list:
		if CS.legal_move(piece_pos):

			attack_piece = board[piece_pos[0]][piece_pos[1]]
			attack_piece = attack_piece - attack_piece % 2
			
			if attack_piece is not 0 and attack_piece % 2 is enemy:
				if piece > attack_piece:
					return -15
				elif piece < attack_piece:
					return -7
				else
					return 0


def queen_check(pos, board, list, limit_player):
    directions = [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for direction in directions:
        directional_check(pos, board, direction, 8, list, limit_player)


def directional_check(pos, board, direction, step_size, list, limit_player):
    
    new_pos = (pos[0] + direction[0], pos[1] + direction[1])
    new_piece = board[new_pos[0]][[new_pos[1]]]
    
    while legal_move(new_pos) and (new_piece == 0 or new_piece % 2 != limit_player) and step_size != 0:
        
        if new_piece % 2 == limit_player and new_piece != 0:
        	list.append(new_pos)
        	break
        
        new_pos[0] += direction[0]
        new_pos[1] += direction[1]
        new_piece = board[new_pos[0]][new_pos[1]]
        step_size -= 1
