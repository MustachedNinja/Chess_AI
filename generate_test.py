import unittest
import GenerateMoves as MOVES


class TestMoves(unittest.TestCase):
	def setUp(self):
		pass

	def test_pawn_simple():
		test_board = 
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [100,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0]]

		actual_list = MOVES.generate_moves(0, test_board)
		expected_list = [[(6, 0), (5, 0)], [(6, 0), (4, 0)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

		test_board = 
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,100,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0]]

		actual_list = MOVES.generate_moves(0, test_board)
		expected_list = [[(4, 1), (3, 1)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

	def test_pawn_capture():
		test_board = 
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [101,  0,101,  0,  0,  0,  0,  0],
		 [  0,100,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0]]

		actual_list = MOVES.generate_moves(0, test_board)
		expected_list = [[(4, 1), (3, 1)], [(4, 1), (3, 0)], [(4, 1), (3, 2)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

	def test_knight_simple():
		test_board = 
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,320,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0]]

		actual_list = MOVES.generate_moves(0, test_board)
		expected_list = [[(4, 3), (6, 2)], [(4, 3), (6, 4)], [(4, 3), (2, 2)], [(4, 3), (2, 4)], 
		[(4, 3), (3, 1)], [(4, 3), (3, 5)], [(4, 3), (5, 1)], [(4, 3), (5, 5)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

	def test_knight_capture():
		test_board = 
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,101,  0,  0,  0,  0,  0,  0],
		 [  0,  0,101,  0,  0,  0,  0,  0],
		 [320,  0,  0,  0,  0,  0,  0,  0]]

		actual_list = MOVES.generate_moves(0, test_board)
		expected_list = [[(7, 0), (5, 1)], [(7, 0), (6, 2)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

	def test_bishop_simple():
		test_board = 
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,330,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0]]

		actual_list = MOVES.generate_moves(0, test_board)
		expected_list = [[(6, 3), (5, 2)], [(6, 3), (5, 4)], [(6, 3), (4, 1)], 
		[(6, 3), (4, 5)], [(6, 3), (3, 0)], [(6, 3), (3, 6)], [(6, 3), (2, 7)],
		[(6, 3), (7, 2)], [(6, 3), (7, 4)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

	def test_bishop_capture():
		test_board = 
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,101,  0,101,  0,  0,  0],
		 [  0,  0,  0,330,  0,  0,  0,  0],
		 [  0,  0,101,  0,101,  0,  0,  0]]

		actual_list = MOVES.generate_moves(0, test_board)
		expected_list = [[(6, 3), (5, 2)], [(6, 3), (5, 4)], [(6, 3), (7, 2)], [(6, 3), (7, 4)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

	def test_rook_simple():
		test_board = 
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,500,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0]]

		actual_list = MOVES.generate_moves(0, test_board)
		expected_list = [[(6, 1), (6, 0)], [(6, 1), (6, 2)], [(6, 1), (6, 3)], [(6, 1), (6, 4)], 
		[(6, 1), (6, 5)], [(6, 1), (6, 6)], [(6, 1), (6, 7)], [(6, 1), (7, 1)], [(6, 1), (5, 1)], 
		[(6, 1), (4, 1)], [(6, 1), (3, 1)], [(6, 1), (2, 1)], [(6, 1), (1, 1)], [(6, 1), (0, 1)]] 

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

	def test_rook_capture():
		test_board = 
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,101,  0,  0,  0,  0,  0,  0],
		 [101,500,101,  0,  0,  0,  0,  0],
		 [  0,101,  0,  0,  0,  0,  0,  0]]

		actual_list = MOVES.generate_moves(0, test_board)
		expected_list = [[(6, 1), (6, 0)], [(6, 1), (6, 3)], [(6, 1), (5, 1)], [(6, 1), (7, 1)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list
	def test_queen_simple():
		test_board = 
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,980,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0]]

		actual_list = MOVES.generate_moves(0, test_board)
		expected_list = [[(6, 1), (6, 0)], [(6, 1), (6, 2)], [(6, 1), (6, 3)], [(6, 1), (6, 4)], 
		[(6, 1), (6, 5)], [(6, 1), (6, 6)], [(6, 1), (6, 7)], [(6, 1), (7, 1)], [(6, 1), (5, 1)], 
		[(6, 1), (4, 1)], [(6, 1), (3, 1)], [(6, 1), (2, 1)], [(6, 1), (1, 1)], [(6, 1), (0, 1)],
		[(6, 1), (5, 0)], [(6, 1), (5, 2)], [(6, 1), (7, 0)], [(6, 1), (7, 2)], [(6, 1), (4, 3)],
		[(6, 1), (3, 4)], [(6, 1), (2, 5)], [(6, 1), (1, 6)], [(6, 1), (0, 7)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

	def test_queen_capture():
		test_board = 
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [101,101,101,  0,  0,  0,  0,  0],
		 [101,980,101,  0,  0,  0,  0,  0],
		 [101,101,101,  0,  0,  0,  0,  0]]

		actual_list = MOVES.generate_moves(0, test_board)
		expected_list = [[(6, 1), (6, 0)], [(6, 1), (6, 2)], [(6, 1), (5, 0)], [(6, 1), (5, 1)],
		[(6, 1), (5, 2)], [(6, 1), (7, 0)], [(6, 1), (7, 1)], [(6, 1), (7, 2)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list


	def test_king_simple():
		test_board = 
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,40000,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0]]

		actual_list = MOVES.generate_moves(0, test_board)
		expected_list = [[(6, 1), (6, 0)], [(6, 1), (6, 2)], [(6, 1), (5, 0)], [(6, 1), (5, 1)],
		[(6, 1), (5, 2)], [(6, 1), (7, 0)], [(6, 1), (7, 1)], [(6, 1), (7, 2)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

	def test_king_capture():
		test_board = 
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [101,101,101,  0,  0,  0,  0,  0],
		 [101,40000,101,  0,  0,  0,  0,  0],
		 [101,101,101,  0,  0,  0,  0,  0]]

		actual_list = MOVES.generate_moves(0, test_board)
		expected_list = [[(6, 1), (6, 0)], [(6, 1), (6, 2)], [(6, 1), (5, 0)], [(6, 1), (5, 1)],
		[(6, 1), (5, 2)], [(6, 1), (7, 0)], [(6, 1), (7, 1)], [(6, 1), (7, 2)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list
