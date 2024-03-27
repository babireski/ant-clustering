import random

class Ant:
    def __init__(self, sight, place):
        self.sight = sight
        self.place = place
        self.state = False
        self.k = (1, 1)

    def __eq__(self, other):
        return self.place == other.place

    def work(self, grid):
        self.drop(grid) if self.state else self.pick(grid)
        neighbours = [place for place in self.neighbours(grid, 1) if place not in map(lambda ant: ant.place, grid.ants)]
        if len(neighbours) > 0:
            self.place = random.choice(neighbours)

    def pick(self, grid):
        if self.place in grid.data:
            neighbours = len(self.neighbours(grid, self.sight, data = True))
            vision = (self.sight * 2 + 1) ** 2 - 1
            probability = 1 - (neighbours / vision) ** 2
            if random.uniform(0, 1) < probability:
                self.state = True
                grid.data.remove(self.place)

    def drop(self, grid):
        if self.place not in grid.data:
            neighbours = len(self.neighbours(grid, self.sight, data = True))
            vision = (self.sight * 2 + 1) ** 2 - 1
            probability = (neighbours / vision) ** 2
            if random.uniform(0, 1) < probability:
                self.state = False
                grid.data.append(self.place)

    def neighbours(self, grid, sight, data = False):
        x, y = self.place
        neighbours = [((x + 1) % grid.size, (y + 1) % grid.size), ((x + 1) % grid.size, y), ((x + 1) % grid.size, (y - 1 + grid.size) % grid.size), (x, (y + 1) % grid.size), (x, y - 1), ((x - 1 + grid.size) % grid.size, (y + 1) % grid.size), ((x - 1 + grid.size) % grid.size, y), ((x - 1 + grid.size) % grid.size, (y - 1 + grid.size) % grid.size)]
        if data:
            return list(set(grid.data).intersection(neighbours))
        return neighbours

    def similarity(self, grid):
        neighbours = len(list(set(grid.data).intersection(self.neighbours(grid))))
        return 1 / neighbours ** 2 if neighbours > 0 else 0