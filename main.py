from Figure import Figure
from Board import Board
from EmptyField import EmptyField
from Bishop import Bishop


def print_array(array):
    string = "  "
    for i in range(8):
        string += str(i) + "  "

    print(string)
    for i in range(8):
        print(i, end="")
        print(array[i])

board = []
for i in range(8):
    row = []
    for j in range(8):
        null = EmptyField([i, j], " ")
        row.append(null)
    board.append(row)

bishop = Bishop([1, 1], "P", False, "B")
board[1][1] = bishop
bishop2 = Bishop([2, 2], "P", True, "b")
board[2][2] = bishop2

print_array(board)
print(bishop.check_next_field(board))
