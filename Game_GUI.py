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
import time
from SoundsPlayer import play_sound
import copy

CHECKMATE = 100000
DRAW = 0

class Game_Gui:
    def __init__(self):
        self._board = Board()
        self._time = 0
        self._winner_message = ""
        self._result = 2
        self._chess_notation = []
        self._broken_figures_W = []
        self._broken_figures_B = []
        self._main_depth = 3
        self._ai_next_move = []
        self._deepcopy_time = 0
        # self.create_players()

    def get_deepcopy_time(self):
        return self._deepcopy_time

    def create_players(self):
        self._playerW = Player(True)
        self._playerB = Player(False)

    def get_board(self):
        return self._board

    def get_time(self):
        return self._time

    def get_winner_message(self):
        return self._winner_message

    def get_result(self):
        return self._result

    def get_playerW(self):
        return self._playerW

    def get_playerB(self):
        return self._playerB

    def get_chess_notation(self):
        return self._chess_notation

    def get_broken_figures_W(self):
        return self._broken_figures_W

    def get_broken_figures_B(self):
        return self._broken_figures_B

    def get_ai_next_move(self):
        return self._ai_next_move

    def set_time(self, new_time):
        self._time = new_time

    def set_chess_notation(self, new_chess_notation):
        self._chess_notation = new_chess_notation

    def set_result(self, new_result):
        self._result = new_result

    def set_winner_message(self, new_message):
        self._winner_message = new_message

    def check_choosen_figure(self, player, pos):
        figure = self._board.get_array()[pos[0]][pos[1]]

        if figure.get_name() != " " and figure.get_team() == player.get_team():
            next_fields_list = figure.check_next_field(self._board)
            if len(next_fields_list):
                return True
        return False

    def check_move(self, old_position, new_position):
        next_fields_list = self._board.get_next_fields_list(old_position)
        for next_field in next_fields_list:
            if next_field == new_position:
                return True
        return False

    def check_if_pawn_converting(self, new_position):
        # if self._board.get_array()[new_position[0]][new_position[1]].get_name().lower() == "p" and (new_position[0] == 0 or new_position[0] == 7):
        #     return True
        # return False
        if self._board.get_pawn_converted():
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

    def add_to_broken_figures(self, figure):
        if figure.get_team():
            self._broken_figures_W.append(figure)
        else:
            self._broken_figures_B.append(figure)

    def find_board_weight(self, board):
        if board.is_checkmate(True):
            return -CHECKMATE
        elif board.is_checkmate(False):
            return CHECKMATE

        if board.check_if_draw(self._chess_notation):
            return DRAW

        weight = 0
        for i in range(8):
            for j in range(8):
                figure = board.get_array()[i][j]
                if figure.get_name() == " ":
                    continue
                if figure.get_team():
                    weight += figure.get_weight()
                else:
                    weight -= figure.get_weight()
        return weight

    def find_weight(self, board):
        # a = time.time()
        weight = 0
        for i in range(8):
            for j in range(8):
                figure = board.get_array()[i][j]
                if figure.get_name() == " ":
                    continue
                weight += figure.get_weight()
        # b = time.time()
        # self._deepcopy_time += (b-a)
        return weight

    # def find_the_best_move(self, team, depth, alpha, beta):
    #     if depth == 0:
    #         return self.find_weight(self.get_board())

    #     if team:
    #         max_weight = -CHECKMATE
    #     else:
    #         max_weight = CHECKMATE

    #     for i in range(8):
    #         for j in range(8):
    #             figure = self.get_board().get_array()[i][j]
    #             if figure.get_name() != " " and figure.get_team() == team:
    #                 valid_moves = self._board.get_next_fields_list([i, j])
    #                 for move in valid_moves:
    #                     board_copy = copy.deepcopy(self._board)
    #                     self.get_board().change_figure_position([i, j], move)
    #                     new_weight = self.find_the_best_move(not team, depth - 1, alpha, beta)
    #                     if team:
    #                         if new_weight > max_weight:
    #                             max_weight = new_weight
    #                             if depth == self._main_depth:
    #                                 self._ai_next_move = [[i, j], move]
    #                     else:
    #                         if new_weight < max_weight:
    #                             max_weight = new_weight
    #                             if depth == self._main_depth:
    #                                 self._ai_next_move = [[i, j], move]
    #                     self._board = board_copy


    #                     if team:
    #                         if max_weight > alpha:
    #                             alpha = max_weight
    #                     else:
    #                         if max_weight < beta:
    #                             beta = max_weight
    #                     if alpha >= beta:
    #                         break



    #     return max_weight

    def find_the_best_move(self, depth, possible_moves, alpha, beta, team_num):
        if depth == 0:
            return team_num * self.find_board_weight(self._board)
        
        max_weight = -CHECKMATE
        for move in possible_moves:
            figure_pos = [move[2], move[3]]
            next_move = [move[0], move[1]]
            board_copy = copy.deepcopy(self._board)
            
            self._board.change_figure_position(figure_pos, next_move)
            a = time.time()
            new_possible_moves = self._board.get_all_possible_moves(True if team_num == 1 else False)
            b = time.time()
            self._deepcopy_time += (b-a)
            new_weight = -self.find_the_best_move(depth - 1, new_possible_moves, -beta, -alpha, -team_num)
            if new_weight > max_weight:
                max_weight = new_weight
                if depth == self._main_depth:
                    self._ai_next_move = [figure_pos, next_move]
            self._board = board_copy
            if max_weight > alpha:
                alpha = max_weight
            if alpha >= beta:
                break
        return max_weight

        

    def move(self, old_position, new_position):
        next_fields_list = self._board.get_next_fields_list(old_position)
        castling_fields = self._board.get_castling_fields(old_position)

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
