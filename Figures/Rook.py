from Figures.Figure import Figure

class Rook(Figure):
    def __init__(self, name, position, picture, team):
        super().__init__(name, position, picture, team)
        self._combinations = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self._long_step_move = True

    # TODO castling - zrobić roszadę wieży i króla