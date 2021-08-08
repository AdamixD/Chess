from Board import Board
from Figures.EmptyField import EmptyField
from time import time

class Game:
    def __init__(self, playerW, playerB):
        self._board = Board()
        self._time = 0
        self._message = ""
        self._playerW = playerW
        self._playerB = playerB

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
            old_x, old_y = list(map(int, input().split()))
            figure = self._board.get_array()[old_x][old_y]
            if figure.get_team() == player.get_team():
                is_ok = True

        next_fields_list = figure.check_next_field(self._board)

        is_ok = False
        while not is_ok:
            new_position = list(map(int, input().split()))
            new_x, new_y = new_position
            for next_field in next_fields_list:
                if next_field == new_position:
                    is_ok = True
                    figure = self._board.get_array()[new_x][new_y]
                    # TODO
                    if not figure.get_name() == " ":
                        pass

                    self._board.change_figure_position([old_x, old_y], new_position)


    def play(self):
        checkmateW = False
        checkmateB = False
        # round True is for white
        round = True
        while not checkmateW and not checkmateB:
            if round:
                self.move(self._playerW)
            else:
                self.move(self._playerB)

            round != round




