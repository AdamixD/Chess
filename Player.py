class Player:
    def __init__(self, team):
        self._team = team
        self._score = 0
        self.create_name()

    def create_name(self):
        team_text = "Black"
        if self._team:
            team_text = "White"
        name = input(f"Player {team_text}, what is your name?:  ")
        self._name = name

    def get_name(self):
        return self._name

    def get_team(self):
        return self._team

    def get_score(self):
        return self._score

    def won(self):
        self._score += 1
