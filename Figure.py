class Figure:
    def __init__(self, position, picture, team, name):
        self._position = position
        self._picture = picture
        self._team = team
        self._name = name

    def get_position(self):
        return self._position

    def get_picture(self):
        return self._picture

    def get_team(self):
        return self._team

    def get_name(self):
        return self._name

    def set_position(self, new_position):
        self._position = new_position

    def __str__(self):
        return self._name

    def __repr__(self):
        return self._name
