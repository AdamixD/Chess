from Figures.Knight import Knight
from Figures.Rook import Rook
from Figures.King import King
from Figures.Pawn import Pawn
from Figures.Queen import Queen
from Figures.Bishop import Bishop
from Figures.EmptyField import EmptyField
from Board import Board
from Player import Player
from time import time

class Game:
    def __init__(self):
        self._board = Board()
        self._time = 0
        self._message = ""
        self.create_players()

    def create_players(self):
        self._playerW = Player(True, 1)
        self._playerB = Player(False, 1)

    def get_board(self):
        return self._board

    def get_time(self):
        return self._time

    def get_message(self):
        return self._message

    def get_playerW(self):
        return self._playerW

    def get_playerB(self):
        return self._playerB

    def set_time(self, new_time):
        self._time = new_time

    def set_message(self, new_message):
        self._message = new_message

    def move(self, player):
        old_x, old_y = 0, 0
        figure = EmptyField([0, 0], " ")

        is_ok = False
        while not is_ok:
            print(f"1 choose figure: ")
            old_x, old_y = list(map(int, input().split()))

            figure = self._board.get_array()[old_x][old_y]

            if figure.get_team() == player.get_team():
                next_fields_list = figure.check_next_field(self._board)
                if len(next_fields_list):
                    is_ok = True

            elif figure.get_team() != player.get_team() and figure.get_name() != " ":
                print("It is not your figure")
            else:
                print("Choose another figure")

        castling_fields = []
        if figure.get_name().lower() == "k":
            castling_fields = figure.if_castling(self._board)
            for new_field in castling_fields:
                next_fields_list.append(new_field)

        print(f"1 you can move this figure to: {next_fields_list}")

        is_ok = False
        new_figure = None

        while not is_ok:
            print(f"1 choose field to move on: ")
            new_position = list(map(int, input().split()))
            new_x, new_y = new_position

            for next_field in next_fields_list:
                if next_field == new_position:
                    is_ok = True
                    if next_field in castling_fields:
                        self._board.castling(next_field)
                        break
                    # if figure.get_name().lower() == "p":
                    #     delta = abs(new_position[0] - figure.get_position()[0])
                    #     if  delta == 2:
                    #         figure.set_two_step_move(True)
                    #     else:
                    #         figure.set_two_step_move(False)

                    if figure.get_name().lower() == "p" and (new_position[0] == 0 or new_position[0] == 7):
                        new_figure_name = input(f"1, your pawn will convert to (r, n, b, q): ")

                        if new_figure_name == "r":
                            if player.get_team():
                                new_figure = Rook("R", new_position, "Images/Rook_W.png", True)
                            else:
                                new_figure = Rook("r", new_position, "Images/Rook_B", False)
                        elif new_figure_name == "n":
                            if player.get_team():
                                new_figure = Knight("N", new_position, "Images/Knight_W.png", True)
                            else:
                                new_figure = Knight("n", new_position, "Images/Knight_B.png", False)
                        elif new_figure_name == "b":
                            if player.get_team():
                                new_figure = Bishop("B", new_position, "Images/Bishop_W.png", True)
                            else:
                                new_figure = Bishop("b", new_position, "Images/Bishop_B.png", False)
                        else:
                            if player.get_team():
                                new_figure = Queen("Q", new_position, "Images/Queen_W.png", True)
                            else:
                                new_figure= Queen("q", new_position, "Images/Queen_B.png", False)


                    figure = self._board.get_array()[new_x][new_y]
                    # TODO
                    if not figure.get_name() == " ":
                        pass

                    self._board.change_figure_position([old_x, old_y], new_position)
                    if new_figure:
                        self._board.addFigure(new_figure)
                    break

            if not is_ok:
                print("This figure can't go to this field. Try another.")

    def play(self):
        checkmateW = False
        checkmateB = False
        winner = None
        # round True is for white
        round = True
        while True:
            self._board.print_board()
            if round:
                round = False
                self.move(self._playerW)
                if self._board.is_checkmate(False):
                    winner = self._playerW
                    break
            else:
                round = True
                self.move(self._playerB)
                if self._board.is_checkmate(True):
                    winner = self._playerB
                    break

        winner.won()
        print(f"{winner.get_name()} won this round")





