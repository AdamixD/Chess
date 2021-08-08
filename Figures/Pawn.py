from Figures.Figure import Figure

class Pawn(Figure):
    def __init__(self, position, picture, team, name, is_moved = False):
        super().__init__(position, picture, team, name)
        self._is_moved = is_moved
        self._long_step_move = False

    def get_is_moved(self):
        return self._is_moved

    def set_is_moved(self, is_moved):
        self._is_moved = is_moved

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
            if new_x >= 0 and new_x < 8:
                if board_array[new_x][y].get_name() == " ":
                    if self.check_if_check(board, [new_x, y]):
                        continue
                    array.append([new_x, y])
                else:
                    if board_array[new_x][y].get_team() != self._team:
                        if self.check_if_check(board, [new_x, y]):
                            continue
                        array.append([new_x, y])

        return array