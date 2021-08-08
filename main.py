from Figures.Figure import Figure
from Figures.Bishop import Bishop
from Figures.Pawn import Pawn
from Board import Board

board = Board()
board.print_board()

# board.change_figure_position([1, 3], [2, 3])
# board.change_figure_position([6, 4], [5, 4])
# board.change_figure_position([7, 5], [3, 1])
# board.print_board()

# print(board.get_array()[0][6].check_next_field(board))
# print(board.get_array()[1][2].check_next_field(board))
# print(board.get_array()[1][7].check_next_field(board))
# print(board.get_array()[0][2].check_next_field(board))
# print(board.get_array()[0][1].check_next_field(board))

#checking checkmate
board.change_figure_position([6, 4], [5, 4])
board.print_board()
board.change_figure_position([1, 4], [2, 4])
board.print_board()
board.change_figure_position([7, 3], [4, 7])
board.print_board()
board.change_figure_position([0, 1], [2, 0])
board.print_board()
board.change_figure_position([7, 5], [4, 2])
board.print_board()
board.change_figure_position([2, 0], [0, 1])
board.print_board()
board.change_figure_position([4, 7], [1, 5])
board.print_board()

print(board.is_checkmate(False))

# print(board.is_check(False))
