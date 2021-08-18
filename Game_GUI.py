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
from SoundsPlayer import play_sound

class Game_Gui:
    def __init__(self):
        self._board = Board()
        self._time = 0
        self._winner_message = ""
        self._chess_notation = []
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

    def get_chess_notation(self):
        return self._chess_notation

    def set_chess_notation(self, new_chess_notation):
        self._chess_notation = new_chess_notation

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

    def create_notation_item(self, old_pos, new_pos):
        string = ""
        figure = self._board.get_array()[old_pos[0]][old_pos[1]]
        if figure.get_name().lower() != "p":
            string += figure.get_name().upper()
        string += chr(old_pos[1] + 97)
        string += str(old_pos[0] + 1)

        new_pos_figure = self._board.get_array()[new_pos[0]][new_pos[1]]
        if new_pos_figure.get_name() != " ":
            string += "x"
        else:
            string += "-"
        string += chr(new_pos[1] + 97)
        string += str(new_pos[0] + 1)

        return string

    def set_check_notation(self):
        notation = self._chess_notation
        notation[len(notation)-1] += "+"
        self._chess_notation = notation

    def set_checkmate_notation(self):
        notation = self._chess_notation
        notation[len(notation)-1] += "#"
        self._chess_notation = notation

    def move(self, old_position, new_position):
        next_fields_list = self.get_next_fields_list(old_position)
        castling_fields = self.get_castling_fields(old_position)

        for next_field in next_fields_list:
            if next_field == new_position:
                if next_field in castling_fields:
                    self._board.castling(next_field)
                    if new_position[1] < old_position[1]:
                        self._chess_notation.append("0-0-0")
                    else:
                        self._chess_notation.append("0-0")
                    play_sound("Sounds/Castling.mp3", 0.135)
                    break
                if self._board.get_array()[next_field[0]][next_field[1]].get_name() != " ":
                    play_sound("Sounds/Beat.mp3")
                else:
                    play_sound("Sounds/Moving.mp3")
                self._chess_notation.append(self.create_notation_item(old_position, new_position))
                self._board.change_figure_position(old_position, new_position)
                break
