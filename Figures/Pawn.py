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
        y = self._position[0]
        x = self._position[1]

        step = 1
        if not self._team:
            step = -1

        new_y = y

        number_of_steps = 2
        if self._is_moved:
            number_of_steps = 1

        for i in range(number_of_steps):
            new_y += step
            if new_y >= 0 and new_y < 8:
                if board[x][new_y].get_name() == " ":
                    array.append([x, new_y])
                else:
                    if board[x][new_y].get_team() != self._team:
                        array.append([x, new_y])

        return array