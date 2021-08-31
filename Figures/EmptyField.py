class EmptyField:
    def __init__(self, position, name):
        self._position = position
        self._name = name
        self._weight = 0

    def get_position(self):
        return self._position

    def get_name(self):
        return self._name

    def set_position(self, new_position):
        self._position = new_position

    def get_weight(self):
        return self._weight
    
    def __str__(self):
        return self._name

    def __repr__(self):
        return self._name

