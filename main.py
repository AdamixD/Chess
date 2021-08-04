from Figures.Bishop import Bishop
from Figures.Figure import Figure

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
        null = Figure(" ", [i, j])
        row.append(null)
    board.append(row)

bishop = Bishop("B", [1, 1], "Image", False)
board[1][1] = bishop
# bishop2 = Bishop("b", [1, 1], "Image", False)
# board[2][2] = bishop2

print_array(board)
print(bishop.check_next_field(board))
