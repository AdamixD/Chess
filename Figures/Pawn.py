from Figures.Figure import Figure

class Pawn(Figure):
    def __init__(self, name, position, picture, team, is_moved = False):
        super().__init__(name, position, picture, team)
        self._is_moved = is_moved
        self._long_step_move = False

    def get_is_moved(self):
        return self._is_moved

    def set_is_moved(self):
        self._is_moved = True

    def check_next_field_simple(self, board):
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
            if new_x >= 0 and new_x < 8:
                if board_array[new_x][y].get_name() == " ":
                    array.append([new_x, y])
                if i == 0:
                    if y+step<8 and y+step>=0 and board_array[new_x][y+step].get_name() != " " and board_array[new_x][y+step].get_team() != self._team:
                        array.append([new_x, y+step])

                    if y-step>=0 and y-step<8 and board_array[new_x][y-step].get_name() != " " and board_array[new_x][y-step].get_team() != self._team:
                        array.append([new_x, y-step])
        return array

    def check_next_field(self, board):
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
                    if self.check_if_check(board, [new_x, y]):
                        continue
                    array.append([new_x, y])
                if i == 0:
                    if y+step<8 and y+step>=0 and board_array[new_x][y+step].get_name() != " " and board_array[new_x][y+step].get_team() != self._team:
                        if not self.check_if_check(board, [new_x, y+step]):
                            array.append([new_x, y+step])

                    if y-step>=0 and y-step<8 and board_array[new_x][y-step].get_name() != " " and board_array[new_x][y-step].get_team() != self._team:
                        if not self.check_if_check(board, [new_x, y-step]):
                            array.append([new_x, y-step])

        return array