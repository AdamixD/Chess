from Figures.Figure import Figure

class Knight(Figure):
    def __init__(self, name, position, picture, team):
        super().__init__(name, position, picture, team)
        self._combinations = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
        self._long_step_move = False
        self._weight = 30
        if not team:
            self._weight = -30
