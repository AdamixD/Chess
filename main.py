from Figures.Figure import Figure
from Figures.Bishop import Bishop
from Figures.Pawn import Pawn
from Board import Board

board = Board()
board.print_board()

board.change_figure_position([1, 3], [2, 3])
board.change_figure_position([6, 4], [5, 4])
board.change_figure_position([7, 5], [3, 1])
board.print_board()

print(board.get_array()[3][1].check_next_field(board.get_array()))
print(board.is_check(False))
