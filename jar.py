from pebble import Pebble


class Jar:
    def __init__(self):
        self._pebbles = []
        self._counter = 0

    def contents(self):
        return list(self._pebbles)
