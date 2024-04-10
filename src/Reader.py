import seaborn

class Reader:
    def __init__(self, filepath, wrapper, colormap, clusters, normalize = False):
        self.filepath = filepath
        self.wrapper = wrapper
        self.colormap = seaborn.color_palette(colormap, clusters).as_hex()
        self.data = []
        self.read()
        if normalize:
            self.normalize()

    def read(self):
        with open(self.filepath, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line[0] != '\n' and line[0] != '\t' and line[0] != '#':
                    data = line.split()
                    data.append(self.colormap)
                    self.data.append(self.wrapper(*data))

    def normalize(self):
        maximums = [float('-inf'), float('-inf')]
        minimums = [float('inf'), float('inf')]
        for datum in self.data:
            if datum.x > maximums[0]:
                maximums[0] = datum.x
            if datum.x < minimums[0]:
                minimums[0] = datum.x
            if datum.y > maximums[1]:
                maximums[1] = datum.y
            if datum.y < minimums[1]:
                minimums[1] = datum.y
        for datum in self.data:
            datum.x = (datum.x - minimums[0]) / (maximums[0] - minimums[0])
            datum.y = (datum.y - minimums[1]) / (maximums[1] - minimums[1])
