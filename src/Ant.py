import random

class Ant:
    def __init__(self, sight, place):
        self.sight = sight
        self.place = place
        self.datum = None
        self.alpha = 0.35
        self.k = (0.5, 0.025)

    def __eq__(self, other):
        return self.place == other.place

    def work(self, grid):
        self.drop(grid) if self.datum else self.pick(grid)
        neighbours = [place for place in self.neighbours(grid, 1) if place not in map(lambda ant: ant.place, grid.ants)]
        if len(neighbours) > 0:
            self.place = random.choice(neighbours)

    def pick(self, grid):
        if self.place in grid.data:
            # neighbours = len(self.neighbours(grid, self.sight, data = True))
            # vision = (self.sight * 2 + 1) ** 2 - 1
            # probability = 1 - (neighbours / vision) ** 2
            similarity = self.similarity(grid.data[self.place], grid)
            probability = (self.k[0] / (self.k[0] + similarity)) ** 2
            if random.uniform(0, 1) < probability:
                self.datum = grid.data.pop(self.place)

    def drop(self, grid):
        if not self.place in grid.data:
            # neighbours = len(self.neighbours(grid, self.sight, data = True))
            # vision = (self.sight * 2 + 1) ** 2 - 1
            # probability = (neighbours / vision) ** 2
            similarity = self.similarity(self.datum, grid)
            probability = (similarity / (self.k[1] + similarity)) ** 2
            if random.uniform(0, 1) < probability:
                grid.data[self.place] = self.datum
                self.datum = None

    def neighbours(self, grid, sight, data = False):
        m, n = grid.height, grid.width
        x, y = self.place
        neighbours = [((x + 1) % m, (y + 1) % n), ((x + 1) % m, y), ((x + 1) % m, (y - 1 + n) % n), (x, (y + 1) % n), (x, y - 1), ((x - 1 + m) % m, (y + 1) % n), ((x - 1 + m) % m, y), ((x - 1 + m) % m, (y - 1 + n) % n)]
        if data:
            return list(set(grid.data.keys()).intersection(neighbours))
        return neighbours

    def similarity(self, datum, grid):
        similarity = 0
        neighbours = self.neighbours(grid, self.sight, data = True)
        for place in neighbours:
            neighbour = grid.data[place]
            similarity = similarity + (1 - datum.distance(neighbour) / self.alpha)
        # if len(neighbours):
        #     similarity = similarity / len(neighbours) ** 2 
        vision = (self.sight * 2 + 1) ** 2 - 1
        similarity = similarity / vision **2
        return similarity if similarity > 0 else 0