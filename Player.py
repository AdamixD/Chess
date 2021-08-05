class Player:
    def __init__(self, name, team):
        self._name = name
        self._team = team
        self._score = 0

    def get_name(self):
        return self._name

    def get_team(self):
        return self._team

    def get_score(self):
        return self._score

    def won(self):
        self._score += 1
