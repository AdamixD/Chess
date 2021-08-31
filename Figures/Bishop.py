from Figures.Figure import Figure

class Bishop(Figure):
    def __init__(self, name, position, picture, team):
        super().__init__(name, position, picture, team)
        self._combinations = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        self._long_step_move = True
        self._weight = 30
        if not team:
            self._weight = -30
