"""
Used to evaluate the static value of a piece at a given position on the board
"""

import ChessState as CS
import GenerateMoves as MOVES

PLAYER = 0


pawn_weights = (
[[ 0,  0,  0,  0,  0,  0,  0,  0],
 [50, 50, 50, 50, 50, 50, 50, 50],
 [10, 10, 20, 30, 30, 20, 10, 10],
 [ 5,  5, 10, 27, 27, 10,  5,  5],
 [ 0,  0,  0, 25, 25,  0,  0,  0],
 [ 5, -5,-10,  0,  0,-10, -5,  5],
 [ 5, 10, 10,-25,-25, 10, 10,  5],
 [ 0,  0,  0,  0,  0,  0,  0,  0]])

knight_weights = (
[[-50,-40,-30,-30,-30,-30,-40,-50],
 [-40,-20,  0,  0,  0,  0,-20,-40],
 [-30,  0, 10, 15, 15, 10,  0,-30],
 [-30,  5, 15, 20, 20, 15,  5,-30],
 [-30,  0, 15, 20, 20, 15,  0,-30],
 [-30,  5, 10, 15, 15, 10,  5,-30],
 [-40,-20,  0,  5,  5,  0,-20,-40],
 [-50,-40,-20,-30,-30,-20,-40,-50]])

bishop_weights = ( 
[[-20,-10,-10,-10,-10,-10,-10,-20],
 [-10,  0,  0,  0,  0,  0,  0,-10],
 [-10,  0,  5, 10, 10,  5,  0,-10],
 [-10,  5,  5, 10, 10,  5,  5,-10],
 [-10,  0, 10, 10, 10, 10,  0,-10],
 [-10, 10, 10, 10, 10, 10, 10,-10],
 [-10,  5,  0,  0,  0,  0,  5,-10],
 [-20,-10,-40,-10,-10,-40,-10,-20]])

king_table = (
[[-30,-40,-40,-50,-50,-40,-40,-30],
 [-30,-40,-40,-50,-50,-40,-40,-30],
 [-30,-40,-40,-50,-50,-40,-40,-30],
 [-30,-40,-40,-50,-50,-40,-40,-30],
 [-20,-30,-30,-40,-40,-30,-30,-20],
 [-10,-20,-20,-20,-20,-20,-20,-10], 
 [ 20, 20,  0,  0,  0,  0, 20, 20],
 [ 20, 30, 10,  0,  0, 10, 30, 20]])

def flip_board(board):
	if PLAYER is 1:
		new_board = [[0, 0, 0, 0, 0, 0, 0, 0] for r in range(8)]
		for row in range(8):
			for col in range(8):
				new_board[row][col] = board[7-row][7-col]
		return new_board
	else:
		return board

def eval_board(board, player):
	global PLAYER
	PLAYER = player

	bishop_count = 0
	board_count = 0
	
	for row in range(8):
		for col in range(8):
			if CS.who(board[row][col]) == PLAYER:
				piece_pos = (row, col)
				piece = board[piece_pos[0]][piece_pos[1]]
				piece -= (piece % 2)

				if piece == MOVES.PAWN:
					piece_val = eval_pawn(piece_pos, board)
				elif piece == MOVES.ROOK:
					piece_val = EVAL.eval_rook(piece_pos, board)
				elif piece == MOVES.KNIGHT:
					piece_val = EVAL.eval_knight(piece_pos, board)
				elif piece == MOVES.BISHOP:
					bishop_count += 1
					piece_val = EVAL.eval_bishop(piece_pos, board)
				elif piece == MOVES.QUEEN:
					piece_val = EVAL.eval_queen(piece_pos, board)
				elif piece == MOVES.KING:
					piece_val = EVAL.eval_king(piece_pos, board)
				board_count += piece_val
	if bishop_count is 2:
		board_count += 10
	return board_count


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


def eval_pawn(pos, board):
	score = CS.PAWN
	eval_board = flip_board(board)
	if PLAYER is 1:
		eval_pos = (7 - pos[0], 7 - pos[1])
	else:
		eval_pos = pos
	score += pawn_weights[eval_pos[0]][eval_pos[1]]
	score += eval_piece(eval_pos, eval_board)
	return score


def eval_rook(pos, board):
	score = CS.ROOK
	eval_board = flip_board(board)
	if PLAYER is 1:
		eval_pos = (7 - pos[0], 7 - pos[1])
	else:
		eval_pos = pos
	score += eval_piece(eval_pos, eval_board)
	return score


def eval_knight(pos, board):
	score = CS.KNIGHT
	eval_board = flip_board(board)
	if PLAYER is 1:
		eval_pos = (7 - pos[0], 7 - pos[1])
	else:
		eval_pos = pos
	score += knight_weights[eval_pos[0]][eval_pos[1]]
	score += eval_piece(eval_pos, eval_board)
	return score

def eval_bishop(pos, board):
	score = CS.BISHOP
	eval_board = flip_board(board)
	if PLAYER is 1:
		eval_pos = (7 - pos[0], 7 - pos[1])
	else:
		eval_pos = pos
	score += bishop_weights[eval_pos[0]][eval_pos[1]]
	score += eval_piece(eval_pos, eval_board)
	return score


def eval_queen(pos, board):
	score = CS.QUEEN
	eval_board = flip_board(board)
	if PLAYER is 1:
		eval_pos = (7 - pos[0], 7 - pos[1])
	else:
		eval_pos = pos
	score += eval_piece(eval_pos, eval_board)
	return score


def eval_king(pos, board):
	score = CS.KING
	eval_board = flip_board(board)
	if PLAYER is 1:
		eval_pos = (7 - pos[0], 7 - pos[1])
	else:
		eval_pos = pos
	score += king_weights[eval_pos[0]][eval_pos[1]]
	score += eval_piece(eval_pos, eval_board)
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
	total_list = total_list + relative_pos
	total_list = total_list + knight_pos
	queen_check(pos, board, total_list, PLAYER)

	piece = board[pos[0]][pos[1]] - PLAYER

	for piece_pos in total_list:
		if legal_move(piece_pos):

			defend_piece = board[piece_pos[0]][piece_pos[1]]
			defend_piece = defend_piece - defend_piece % 2

			if defend_piece is not 0 and defend_piece % 2 is PLAYER:
				if piece > defend_piece:
					return 15
				else:
					return 7
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
	total_list = total_list + relative_pos
	total_list = total_list + knight_pos

	if PLAYER is 1:
		enemy = 0
	else:
		enemy = 1
	
	queen_check(pos, board, total_list, enemy)

	piece = board[pos[0]][pos[1]] - PLAYER

	for piece_pos in total_list:
		if legal_move(piece_pos):

			attack_piece = board[piece_pos[0]][piece_pos[1]]
			attack_piece = attack_piece - attack_piece % 2
			
			if attack_piece is not 0 and attack_piece % 2 is enemy:
				if piece > attack_piece:
					return -15
				else:
					return -8
	return 0


def queen_check(pos, board, list_var, limit_player):
	directions = [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)]
	
	for direction in directions:
		directional_check(pos, board, direction, 8, list_var, limit_player)


def directional_check(pos, board, direction, step_size, list_var, limit_player):
	
	new_pos = (pos[0] + direction[0], pos[1] + direction[1])
	if not legal_move(new_pos):
		return
	new_piece = board[new_pos[0]][new_pos[1]]
	
	while legal_move(new_pos) and (new_piece == 0 or new_piece % 2 != limit_player) and step_size != 0:
		if new_piece % 2 == limit_player and new_piece != 0:
			list_var.append(new_pos)
			break
		
		new_pos = (new_pos[0] + direction[0], new_pos[1] + direction[1])
		if not legal_move(new_pos):
			return
		new_piece = board[new_pos[0]][new_pos[1]]
		step_size -= 1

def legal_move(pos):
	"""
	Checks if a given move is within the bounds of the board
	:param pos: position of move as represented by a tuple [row, col]
	:return: True or false
	"""
	if 0 <= pos[0] < 8 and 0 <= pos[1] < 8:
			return True
	else:
		return False
