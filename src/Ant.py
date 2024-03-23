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
        self.drop(grid) if self.state else self.grab(grid)
        neighbours = [place for place in self.neighbours(grid) if place not in map(lambda ant: ant.place, grid.ants)]
        if len(neighbours) > 0:
            self.place = random.choice(neighbours)

    def grab(self, grid):
        if self.place in grid.data:
            similarity = self.similarity(grid)
            probability = (self.k[0] / (self.k[0]) + similarity) ** 2
            if not random.uniform(0, 1) > probability:
                self.state = True
                grid.data.remove(self.place)

    def drop(self, grid):
        if self.place not in grid.data:
            similarity = self.similarity(grid)
            probability = (similarity / (self.k[1] + similarity)) ** 2
            if not random.uniform(0, 1) > probability:
                self.state = True
                grid.data.append(self.place)

    def neighbours(self, grid):
        x, y = self.place
        return [((x + 1) % grid.size, (y + 1) % grid.size), ((x + 1) % grid.size, y), ((x + 1) % grid.size, (y - 1 + grid.size) % grid.size), (x, (y + 1) % grid.size), (x, y - 1), ((x - 1 + grid.size) % grid.size, (y + 1) % grid.size), ((x - 1 + grid.size) % grid.size, y), ((x - 1 + grid.size) % grid.size, (y - 1 + grid.size) % grid.size)]
    
    def similarity(self, grid):
        neighbours = len(list(set(grid.data).intersection(self.neighbours(grid))))
        return 1 / neighbours ** 2 if neighbours > 0 else 0