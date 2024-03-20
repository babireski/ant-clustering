from Ant import Ant

import random

class Grid:
    def __init__(self, side, size):
        self.side = side
        self.size = size
        self.data = []
        self.ants = []
        self.setup()

    def setup(self):
            coordinates = random.choices([(a, b) for a in range(self.side) for b in range(self.side)], k = self.size[0])
            for coordinate in coordinates:
                self.data.append(coordinate)
            coordinates = random.choices([(a, b) for a in range(self.side) for b in range(self.side)], k = self.size[1])
            for coordinate in coordinates:
                self.ants.append(Ant(1, coordinate))

    def run(self):
        while True:
            for ant in self.ants:
                ant.act()
