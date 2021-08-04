from Figures.Figure import Figure

class Bishop(Figure):
    def __init__(self, name, position, picture, team):
        super().__init__(name, position, picture, team)


    def check_next_field(self, board):
        array = []
        x = self._position[0]
        y = self._position[1]

        combinations = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        for combination in combinations:
            new_x = x + combination[0]
            new_y = y + combination[1]

            while new_x >= 0 and new_x < 8 and new_y >= 0 and new_y < 8:
                if board[new_x][new_y].get_name() == " ":
                    array.append([new_x, new_y])
                else:
                    if board[new_x][new_y].get_team() != self._team:
                        array.append([new_x, new_y])
                    break
                new_x += combination[0]
                new_y += combination[1]
    # def check_next_field(self, board):
    #     array = []
    #     x = self._position[0]
    #     y = self._position[1]

    #     new_x = x + 1
    #     new_y = y + 1
    #     while new_x < 8 and new_y < 8:
    #         if board[new_x][new_y].get_name() == " ":
    #             array.append([new_x, new_y])
    #         else:
    #             if board[new_x][new_y].get_team() != self._team:
    #                 array.append([new_x, new_y])
    #             break
    #         new_x += 1
    #         new_y += 1

    #     new_x = x - 1
    #     new_y = y - 1
    #     while new_x >= 0 and new_y >=0:
    #         if board[new_x][new_y].get_name() == " ":
    #             array.append([new_x, new_y])
    #         else:
    #             if board[new_x][new_y].get_team() != self._team:
    #                 array.append([new_x, new_y])
    #             break
    #         new_x -= 1
    #         new_y -= 1

    #     new_x = x + 1
    #     new_y = y - 1
    #     while new_x < 8 and new_y >= 0:
    #         if board[new_x][new_y].get_name() == " ":
    #             array.append([new_x, new_y])
    #         else:
    #             if board[new_x][new_y].get_team() != self._team:
    #                 array.append([new_x, new_y])
    #             break
    #         new_x += 1
    #         new_y -= 1

    #     new_x = x - 1
    #     new_y = y + 1
    #     while new_x >= 0 and new_y < 8:
    #         if board[new_x][new_y].get_name() == " ":
    #             array.append([new_x, new_y])
    #         else:
    #             if board[new_x][new_y].get_team() != self._team:
    #                 array.append([new_x, new_y])
    #             break
    #         new_x -= 1
    #         new_y += 1
        return array
