from Figures.Bishop import Bishop
from Figures.Figure import Figure


def test_check_next_field_OneBishop():
    board = []
    for i in range(8):
        row = []
        for j in range(8):
            null = Figure(" ", [i, j])
            row.append(null)
        board.append(row)

    bishop = Bishop("B", [1, 1], "Image", False)
    board[1][1] = bishop

    array = bishop.check_next_field(board)
    correct_array = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [2, 0], [0, 2], [0, 0]]

    assert array == correct_array


def test_check_next_field_TwoWBishops():
    board = []
    for i in range(8):
        row = []
        for j in range(8):
            null = Figure(" ", [i, j])
            row.append(null)
        board.append(row)

    bishop1 = Bishop("B", [1, 1], "Image", False)
    board[1][1] = bishop1
    bishop2 = Bishop("B", [1, 1], "Image", False)
    board[2][2] = bishop2

    array = bishop1.check_next_field(board)
    correct_array = [[2, 0], [0, 2], [0, 0]]

    assert array == correct_array


def test_check_next_field_TwoWarsBishops():
    board = []
    for i in range(8):
        row = []
        for j in range(8):
            null = Figure(" ", [i, j])
            row.append(null)
        board.append(row)

    bishop1 = Bishop("B", [1, 1], "Image", False)
    board[1][1] = bishop1
    bishop2 = Bishop("b", [1, 1], "Image", True)
    board[2][2] = bishop2

    array = bishop1.check_next_field(board)
    correct_array = [[2, 2], [2, 0], [0, 2], [0, 0]]

    assert array == correct_array
