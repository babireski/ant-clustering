import math

class Item:
    def __init__(self, x, y, cluster, colormap):
        self.x = float(x)
        self.y = float(y)
        self.cluster = int(cluster)
        self.color = colormap[self.cluster - 1]

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
