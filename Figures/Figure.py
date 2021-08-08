# Black are at the top, are False and small letters
class Figure:
    def __init__(self, name, position, picture="Image", team=False):
        self._name = name
        self._position = position
        self._picture = picture
        self._team = team
        self._combinations = []
        self._long_step_move = False

    def get_position(self):
        return self._position

    def get_picture(self):
        return self._picture

    def get_team(self):
        return self._team

    def get_name(self):
        return self._name

    def set_position(self, new_position):
        self._position = new_position

    # We use this function for function is_check() in class Board
    def check_next_field_simple(self, board):
        array = []
        x = self._position[0]
        y = self._position[1]

        board_array = board.get_array()

        for combination in self._combinations:
            new_x = x + combination[0]
            new_y = y + combination[1]

            if self._long_step_move:
                while new_x >= 0 and new_x < 8 and new_y >= 0 and new_y < 8:
                    if board_array[new_x][new_y].get_name() == " ":
                        array.append([new_x, new_y])
                    else:
                        if board_array[new_x][new_y].get_team() != self._team:
                            array.append([new_x, new_y])
                        break
                    new_x += combination[0]
                    new_y += combination[1]
            else:
                if new_x >= 0 and new_x < 8 and new_y >= 0 and new_y < 8:
                    if board_array[new_x][new_y].get_name() == " ":
                        array.append([new_x, new_y])
                    else:
                        if board_array[new_x][new_y].get_team() != self._team:
                            array.append([new_x, new_y])
        return array

    def check_if_check(self, board, new_position):
        board_copy = board
        board_copy.change_figure_position(self._position, new_position)
        return board_copy.is_check(self._team)

    # This function is used for figures
    def check_next_field(self, board):
        array = []
        x = self._position[0]
        y = self._position[1]

        board_array = board.get_array()
        
        for combination in self._combinations:
            new_x = x + combination[0]
            new_y = y + combination[1]

            if self._long_step_move:
                while new_x >= 0 and new_x < 8 and new_y >= 0 and new_y < 8:
                    if board_array[new_x][new_y].get_name() == " ":
                        if self.check_if_check(board, [new_x, new_y]):
                            continue
                        array.append([new_x, new_y])
                    else:
                        if board_array[new_x][new_y].get_team() != self._team:
                            if self.check_if_check(board, [new_x, new_y]):
                                continue
                            array.append([new_x, new_y])
                        break
                    new_x += combination[0]
                    new_y += combination[1]
            else:
                if new_x >= 0 and new_x < 8 and new_y >= 0 and new_y < 8:
                    if board_array[new_x][new_y].get_name() == " ":
                        if self.check_if_check(board, [new_x, new_y]):
                            continue
                        array.append([new_x, new_y])
                    else:
                        if board_array[new_x][new_y].get_team() != self._team:
                            if self.check_if_check(board, [new_x, new_y]):
                                continue
                            array.append([new_x, new_y])
        return array
    
    def __str__(self):
        return self._name

    def __repr__(self):
        return self._name
