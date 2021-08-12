from Figures.Queen import Queen
from Figures.Bishop import Bishop
from Figures.EmptyField import EmptyField
from Figures.King import King
from Figures.Knight import Knight
from Figures.Pawn import Pawn
from Figures.Rook import Rook

class Board:
    def __init__(self):
        self.create_board()
        self._kingW_position = [7, 4]
        self._kingB_position = [0, 4]

    def create_board(self):
        self._array = []

        for i in range(8):
            row = []
            for j in range(8):
                empty_field = EmptyField([i, j], " ")
                row.append(empty_field)
            self._array.append(row)

        pawnW1 = Pawn("P", [6, 0], "Images/Pawn_W.png", True)
        pawnW2 = Pawn("P", [6, 1], "Images/Pawn_W.png", True)
        pawnW3 = Pawn("P", [6, 2], "Images/Pawn_W.png", True)
        pawnW4 = Pawn("P", [6, 3], "Images/Pawn_W.png", True)
        pawnW5 = Pawn("P", [6, 4], "Images/Pawn_W.png", True)
        pawnW6 = Pawn("P", [6, 5], "Images/Pawn_W.png", True)
        pawnW7 = Pawn("P", [6, 6], "Images/Pawn_W.png", True)
        pawnW8 = Pawn("P", [6, 7], "Images/Pawn_W.png", True)

        pawnB1 = Pawn("p", [1, 0], "Images/Pawn_B.png", False)
        pawnB2 = Pawn("p", [1, 1], "Images/Pawn_B.png", False)
        pawnB3 = Pawn("p", [1, 2], "Images/Pawn_B.png", False)
        pawnB4 = Pawn("p", [1, 3], "Images/Pawn_B.png", False)
        pawnB5 = Pawn("p", [1, 4], "Images/Pawn_B.png", False)
        pawnB6 = Pawn("p", [1, 5], "Images/Pawn_B.png", False)
        pawnB7 = Pawn("p", [1, 6], "Images/Pawn_B.png", False)
        pawnB8 = Pawn("p", [1, 7], "Images/Pawn_B.png", False)

        kingW = King("K", [7, 4], "Images/King_W.png", True)
        kingB = King("k", [0, 4], "Images/King_B.png", False)

        rookW1 = Rook("R", [7, 0], "Images/Rook_W.png", True)
        rookW2 = Rook("R", [7, 7], "Images/Rook_W.png", True)
        rookB1 = Rook("r", [0, 0], "Images/Rook_B.png", False)
        rookB2 = Rook("r", [0, 7], "Images/Rook_B.png", False)

        bishopW1 = Bishop("B", [7, 2], "Images/Bishop_W.png", True)
        bishopW2 = Bishop("B", [7, 5], "Images/Bishop_W.png", True)
        bishopB1 = Bishop("b", [0, 2], "Images/Bishop_B.png", False)
        bishopB2 = Bishop("b", [0, 5], "Images/Bishop_B.png", False)

        knightW1 = Knight("N", [7, 1], "Images/Knight_W.png", True)
        knightW2 = Knight("N", [7, 6], "Images/Knight_W.png", True)
        knightB1 = Knight("n", [0, 1], "Images/Knight_B.png", False)
        knightB2 = Knight("n", [0, 6], "Images/Knight_B.png", False)

        queenW = Queen("Q", [7, 3], "Images/Queen_W.png", True)
        queenB = Queen("q", [0, 3], "Images/Queen_B.png", False)

        self.addFigure(pawnW1)
        self.addFigure(pawnW2)
        self.addFigure(pawnW3)
        self.addFigure(pawnW4)
        self.addFigure(pawnW5)
        self.addFigure(pawnW6)
        self.addFigure(pawnW7)
        self.addFigure(pawnW8)

        self.addFigure(pawnB1)
        self.addFigure(pawnB2)
        self.addFigure(pawnB3)
        self.addFigure(pawnB4)
        self.addFigure(pawnB5)
        self.addFigure(pawnB6)
        self.addFigure(pawnB7)
        self.addFigure(pawnB8)

        self.addFigure(kingW)
        self.addFigure(kingB)

        self.addFigure(bishopW1)
        self.addFigure(bishopW2)
        self.addFigure(bishopB1)
        self.addFigure(bishopB2)

        self.addFigure(rookW1)
        self.addFigure(rookB1)
        self.addFigure(rookW2)
        self.addFigure(rookB2)

        self.addFigure(knightW1)
        self.addFigure(knightW2)
        self.addFigure(knightB1)
        self.addFigure(knightB2)

        self.addFigure(queenW)
        self.addFigure(queenB)

    def get_kingW_position(self):
        return self._kingW_position

    def get_kingB_position(self):
        return self._kingB_position

    def get_array(self):
        return self._array

    def addFigure(self, figure):
        x = figure.get_position()[0]
        y = figure.get_position()[1]

        self._array[x][y] = figure

    def print_board(self):
        string = "  "
        for i in range(8):
            string += str(i) + "  "

        print(string)
        for i in range(8):
            print(i, end="")
            print(self._array[i])

    def change_figure_position(self, old_position, new_position):
        old_x, old_y = old_position
        new_x, new_y = new_position

        if self._array[old_x][old_y].get_name() == "k":
            self._array[old_x][old_y].set_is_moved()
            self._kingB_position = [new_x, new_y]
        elif self._array[old_x][old_y].get_name() == "K":
            self._array[old_x][old_y].set_is_moved()
            self._kingW_position = [new_x, new_y]

        if self._array[old_x][old_y].get_name().lower() == "r":
            self._array[old_x][old_y].set_is_moved()

        if self._array[old_x][old_y].get_name().lower() == "p":
            self._array[old_x][old_y].set_is_moved()

        self._array[old_x][old_y].set_position([new_x, new_y])
        self._array[new_x][new_y] = self._array[old_x][old_y]
        self._array[old_x][old_y] = EmptyField([old_x, old_y], " ")

    def castling(self, new_king_pos):
        row = new_king_pos[0]

        if new_king_pos[1] == 2:
            self.change_figure_position([row, 0], [row, 3])
        elif new_king_pos[1] == 6:
            self.change_figure_position([row, 7], [row, 5])

        self.change_figure_position([row, 4], new_king_pos)

    def is_check(self, team):
        if team:
            king_position = self._kingW_position
        else:
            king_position = self._kingB_position

        for i in range(8):
            for j in range(8):
                figure = self._array[i][j]
                if figure.get_name() != " " and figure.get_team() != team:
                    next_field_list = figure.check_next_field(self, False)
                    for next_field in next_field_list:
                        if next_field == king_position:
                            return True
        return False

    def is_checkmate(self, team):
        if team:
            king_position = self._kingW_position
        else:
            king_position = self._kingB_position


        #check if king has fields to go
        kings_fields_list = self._array[king_position[0]][king_position[1]].check_next_field(self)
        if len(kings_fields_list):
            return False

        for i in range(8):
            for j in range(8):
                figure = self._array[i][j]
                if figure.get_name() != " " and figure.get_team() == team:
                    next_field_list = figure.check_next_field(self)
                    if len(next_field_list):
                        return False
        return True


