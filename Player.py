class Player:
    def __init__(self, team, time, const_time):
        self._team = team
        self._score = 0
        self._time = time
        self._const_time = const_time

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
    
    def get_const_time(self):
        return self._const_time
