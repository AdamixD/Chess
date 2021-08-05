from Figures.Figure import Figure

class Rook(Figure):
    def __init__(self, position, picture, team, name):
        super().__init__(position, picture, team, name)
        self._combinations = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self._long_step_move = True

    # TODO castling - zrobić roszadę wieży i króla