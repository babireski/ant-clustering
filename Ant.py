class Ant:
    def __init__(self, sight, place):
        self.sight = sight
        self.place = place
        self.state = False

    def work(self, grid):
        self.drop(grid) if self.state else self.grab(grid)
        self.move(grid)

    def grab(self, grid):
        self.state = True

    def drop(self, grid):
        self.state = False

    def move(self, grid):
        pass