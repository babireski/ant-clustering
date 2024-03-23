from Ant import Ant

import random

class Grid:
    def __init__(self, size, load):
        self.size = size
        self.load = load
        self.data = []
        self.ants = []
        self.setup()

    def setup(self):
        coordinates = random.sample([(a, b) for a in range(self.size) for b in range(self.size)], k = self.load[0])
        for coordinate in coordinates:
            self.data.append(coordinate)
        coordinates = random.sample([(a, b) for a in range(self.size) for b in range(self.size)], k = self.load[1])
        for coordinate in coordinates:
            self.ants.append(Ant(1, coordinate))

    def run(self):
        for ant in self.ants:
            ant.work(self)
