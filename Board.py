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
        self._pawn_converted = []

    def get_pawn_converted(self):
        return self._pawn_converted

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
            delta = abs(new_position[0] - old_position[0])
            if  delta == 2:
                self._array[old_x][old_y].set_two_step_move(True)
            else:
                self._array[old_x][old_y].set_two_step_move(False)


        if self._array[old_x][old_y].get_name().lower() == "p":
            if self._array[old_x][old_y].get_found_en_passant():
                for en_passant_pos in self._array[old_x][old_y].get_en_passant():
                    if new_position[1] == en_passant_pos[1]:
                        self._array[en_passant_pos[0]][en_passant_pos[1]] = EmptyField([en_passant_pos[0], en_passant_pos[1]], " ")

        self._array[old_x][old_y].set_position([new_x, new_y])
        self._array[new_x][new_y] = self._array[old_x][old_y]
        self._array[old_x][old_y] = EmptyField([old_x, old_y], " ")

        self._pawn_converted = []

        if self._array[new_x][new_y].get_name().lower() == "p":
            if self._array[new_x][new_y].get_team():
                if new_position[0] == 0:
                    queen = Queen("Q", new_position, "Images/Queen_W.png", True)
                    self.addFigure(queen)
                    self._pawn_converted = new_position
            else:
                if new_position[0] == 7:
                    queen = Queen("q", new_position, "Images/Queen_B.png", False)
                    self.addFigure(queen)
                    self._pawn_converted = new_position

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

    def check_if_figures_have_possible_field(self, team):
        if team:
            king_position = self._kingW_position
        else:
            king_position = self._kingB_position

        #check if king has fields to go
        kings_fields_list = self._array[king_position[0]][king_position[1]].check_next_field(self)

        if len(kings_fields_list):
            return True

        for i in range(8):
            for j in range(8):
                figure = self._array[i][j]
                if figure.get_name() != " " and figure.get_team() == team:
                    next_field_list = figure.check_next_field(self)
                    if len(next_field_list):
                        return True
        return False

    def is_checkmate(self, team):
        if self.is_check(team):
            if not self.check_if_figures_have_possible_field(team):
                return True
        return False

    def check_stalemate(self):
        if not self.is_check(True) and not self.is_check(False):
            if not self.check_if_figures_have_possible_field(True) or not self.check_if_figures_have_possible_field(False):
                return True
        return False

    def check_dead_position(self):
        chess_dict = {
            "k" : 0,
            "n" : 1,
            "b" : 2,
        }

        # 0. King, 1. Knightm 2. White-bishop, 3. Black-bishop
        teams = [[0, 0, 0, 0], [0, 0, 0, 0]]
        for i in range(8):
            for j in range(8):
                figure = self._array[i][j]
                figure_name = figure.get_name().lower()
                if figure_name != "b" and figure_name != "n" and figure_name != "k" and figure_name != " ":
                    return False
                elif figure_name != " ":
                    col = 1
                    if figure.get_team():
                        col = 0

                    if figure_name == "b":
                        pos = figure.get_position()
                        delta = (pos[0] + pos[1]) % 2
                        teams[col][2 + delta] += 1
                    else:
                        teams[col][chess_dict[figure_name]] += 1
        combinations = [[[1, 1, 0, 0], [1, 0, 0, 0]], [[1, 0, 0, 0], [1, 1, 0, 0]], [[1, 0, 0, 0], [1, 0, 0, 0]], [[1, 0, 1, 0], [1, 0, 1, 0]], [[1, 0, 0, 1], [1, 0, 0, 1]], [[1, 0, 1, 0], [1, 0, 0, 0]], [[1, 0, 0, 1], [1, 0, 0, 0]], [[1, 0, 0, 0], [1, 0, 1, 0]], [[1, 0, 0, 0], [1, 0, 0, 1]]]
        for combination in combinations:
            if teams == combination:
                return True
        return False

    def check_threefold_repetition(self, history):
        if len(history) > 4:
            last = ""
            count = 0
            for i in range(len(history)-1, -1, -4):
                if last != history[i]:
                    last = history[i]
                    count = 1
                else:
                    count += 1

                if count == 3:
                    return True
        return False

    def check_if_draw(self):
        #Stalemate
        if self.check_stalemate():
            print("Stalemate")
            return True

        #Dead Position
        # if self.check_dead_position():
        #     print("Dead position")
        #     return True

        # #TODO Mutual Agreement
        # #Threefold Repetition
        # if self.check_threefold_repetition(history):
        #     print("3")
        #     return True

        return False
        #TODO 50-Move Rule


