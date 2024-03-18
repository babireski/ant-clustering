import Ant
import Item

import random

class Grid:
    def __init__(self, size, data, population, sight, steps):
        self.size  = size
        self.data  = data
        self.population = population
        self.ants = []
        self.sight = sight
        self.steps = steps

    def setup(self):
            height, width = self.size
            coordinates = random.choices([(a, b) for a in range(height) for b in range(width)], k = len(self.data))
            for coordinate in coordinates:
                for item in self.data:
                    item.position = coordinate
            coordinates = random.choices([(a, b) for a in range(height) for b in range(width)], k = self.population)
            for coordinate in coordinates:
                self.ants.append(Ant(coordinate))

    def run(self):
        while self.steps:
            for ant in self.ants:
                ant.act()