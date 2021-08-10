from Figures.Figure import Figure

class King(Figure):
    def __init__(self, name, position, picture, team, is_moved = False):
        super().__init__(name, position, picture, team)
        self._combinations = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        self._long_step_move = False
        self._is_moved = is_moved

    def if_castling(self, board):
        fields_for_castling = []
        if not self._is_moved:
            array = board.get_array()
            row = self.get_position()[0]

            if array[row][0].get_name().lower() == "r" and not array[row][0].get_is_moved():
                castling = True
                for i in range(1, 4):
                    if array[row][i].get_name() != " ":
                        castling = False
                        break

                if castling:
                    fields_for_castling.append([row, 2])

            if array[row][7].get_name().lower() == "r" and not array[row][7].get_is_moved():
                castling = True
                for i in range(5, 7):
                    if array[row][i].get_name() != " ":
                        castling = False
                        break

                if castling:
                    fields_for_castling.append([row, 6])

        return fields_for_castling

    def get_is_moved(self):
        return self._is_moved

    def set_is_moved(self):
        self._is_moved = True
