from Figures.Figure import Figure

class Rook(Figure):
    def __init__(self, name, position, picture, team, is_moved=False):
        super().__init__(name, position, picture, team)
        self._combinations = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self._long_step_move = True
        self._is_moved = is_moved
        self._weight = 50
        if not team:
            self._weight = -50
    def get_is_moved(self):
        return self._is_moved

    def set_is_moved(self):
        self._is_moved = True
    # TODO castling - zrobić roszadę wieży i króla