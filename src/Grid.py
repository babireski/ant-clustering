from Ant import Ant
from Plotter import Plotter
from Renderer import Renderer

import random

class Grid:
    def __init__(self, size, ants, data, iterations, clusters, plots = [], render = False):
        self.height, self.width = size
        self.iterations = iterations
        self.iteration = 0
        self.ants = []
        self.data = {}
        self.clusters = clusters
        self.plots = plots
        self.render = render
        self.setup(ants, data)

    def setup(self, ants, data):
        coordinates = random.sample([(a, b) for a in range(self.height) for b in range(self.width)], k = len(data))
        for datum in data:
            self.data[coordinates.pop()] = datum
        coordinates = random.sample([(a, b) for a in range(self.height) for b in range(self.width)], k = ants)
        for coordinate in coordinates:
            self.ants.append(Ant(1, coordinate))

    def step(self):
        if self.iteration < self.iterations:
            for ant in self.ants:
                ant.work(self)
            self.iteration = self.iteration + 1
        else:
            if self.ants:
                for ant in self.ants:
                    ant.work(self) if ant.datum else self.ants.remove(ant)

    def run(self):
        if self.render:
            Renderer(self).render()
        else:
            plotter = Plotter(self)
            while self.iteration < self.iterations and self.ants:
                if self.iteration in self.plots:
                    plotter.plot()
                self.step()
            plotter.plot()
