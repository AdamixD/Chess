class Player:
    def __init__(self, team, time):
        self._team = team
        self._score = 0
        self._time = time

    def get_team(self):
        return self._team

    def get_time(self):
        return self._time

    def get_score(self):
        return self._score

    def set_time(self, new_time):
        self._time = new_time

    def won(self):
        self._score += 1
