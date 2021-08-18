from Figures.Figure import Figure

class Pawn(Figure):
    def __init__(self, name, position, picture, team, is_moved = False):
        super().__init__(name, position, picture, team)
        self._is_moved = is_moved
        self._long_step_move = False
        self._two_step_move = False
        self._en_passant = []
        self._found_en_passant = False

    def get_is_moved(self):
        return self._is_moved

    def set_is_moved(self):
        self._is_moved = True

    def get_two_step_move(self):
        return self._two_step_move
    
    def set_two_step_move(self, new_two_step_move):
        self._two_step_move = new_two_step_move
    
    def get_en_passant(self):
        return self._en_passant
    
    def get_found_en_passant(self):
        return self._found_en_passant
    
    def check_next_field(self, board, use_if_check=True):
        array = []
        x = self._position[0]
        y = self._position[1]

        board_array = board.get_array()
        step = -1
        if not self._team:
            step = 1

        new_x = x

        number_of_steps = 2
        if self._is_moved:
            number_of_steps = 1

        for i in range(number_of_steps):
            new_x += step
            if i == 1 and len(array) == 0:
                break
            if new_x >= 0 and new_x < 8:
                if board_array[new_x][y].get_name() == " ":
                    self.next_field_appending(array, use_if_check, board, [new_x, y])
                if i == 0:
                    if y+step<8 and y+step>=0 and board_array[new_x][y+step].get_name() != " " and board_array[new_x][y+step].get_team() != self._team:
                         self.next_field_appending(array, use_if_check, board, [new_x, y+step])

                    if y-step>=0 and y-step<8 and board_array[new_x][y-step].get_name() != " " and board_array[new_x][y-step].get_team() != self._team:
                         self.next_field_appending(array, use_if_check, board, [new_x, y-step])

                    self._found_en_passant = False
                    if y+step<8 and y+step>=0:
                        figure = board_array[x][y+step]
                        if figure.get_name().lower() == "p" and figure.get_team() != self._team and figure.get_two_step_move():
                            self.next_field_appending(array, use_if_check, board, [x+step, y+step])
                            self._en_passant.append([x, y+step])
                            self._found_en_passant = True

                        

                    if y-step>=0 and y-step<8:
                        figure = board_array[x][y-step]
                        if figure.get_name().lower() == "p" and figure.get_team() != self._team and figure.get_two_step_move():
                            self.next_field_appending(array, use_if_check, board, [x+step, y-step])
                            self._en_passant.append([x, y-step])
                            self._found_en_passant = True
                    
                    if not self._found_en_passant:
                        self._en_passant = []
        return array