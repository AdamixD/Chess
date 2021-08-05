from Figures.Figure import Figure

class Knight(Figure):
    def __init__(self, position, picture, team, name):
        super().__init__(position, picture, team, name)
        self._combinations = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
        self._long_step_move = False
