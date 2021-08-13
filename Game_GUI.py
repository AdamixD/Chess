from Figures.Figure import Figure
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

class Game_Gui:
    def __init__(self):
        self._board = Board()
        self._time = 0
        self._winner_message = ""
        # self.create_players()

    def create_players(self):
        self._playerW = Player(True)
        self._playerB = Player(False)

    def get_board(self):
        return self._board

    def get_time(self):
        return self._time

    def get_winner_message(self):
        return self._winner_message

    def get_playerW(self):
        return self._playerW

    def get_playerB(self):
        return self._playerB

    def set_time(self, new_time):
        self._time = new_time

    def set_winner_message(self, new_message):
        self._winner_message = new_message

    def check_choosen_figure(self, player, pos):
        figure = self._board.get_array()[pos[0]][pos[1]]

        if figure.get_name() != " " and figure.get_team() == player.get_team():
            next_fields_list = figure.check_next_field(self._board)
            if len(next_fields_list):
                return True
        return False

    def get_castling_fields(self, pos):
        figure = self._board.get_array()[pos[0]][pos[1]]
        castling_fields = []

        if figure.get_name().lower() == "k":
            castling_fields = figure.if_castling(self._board)
        return castling_fields

    def get_next_fields_list(self, pos):
        figure = self._board.get_array()[pos[0]][pos[1]]
        next_fields_list = figure.check_next_field(self._board)
        castling_fields = self.get_castling_fields(pos)

        for field in castling_fields:
            next_fields_list.append(field)

        return next_fields_list

    def check_move(self, old_position, new_position):
        next_fields_list = self.get_next_fields_list(old_position)
        for next_field in next_fields_list:
            if next_field == new_position:
                return True
        return False

    def check_if_pawn_converting(self, new_position):
        if self._board.get_array()[new_position[0]][new_position[1]].get_name().lower() == "p" and (new_position[0] == 0 or new_position[0] == 7):
            return True
        return False

    def move(self, old_position, new_position):
        next_fields_list = self.get_next_fields_list(old_position)
        castling_fields = self.get_castling_fields(old_position)

        for next_field in next_fields_list:
            if next_field == new_position:
                if next_field in castling_fields:
                    self._board.castling(next_field)
                    break

                self._board.change_figure_position(old_position, new_position)
                break
