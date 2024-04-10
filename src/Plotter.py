import svg

class Plotter():
    def __init__(self, grid):
        self.grid = grid
        self.side = 1000

    def plot(self):
        block = self.side // self.grid.height 
        elements = []
        elements.append(svg.Rect(x = 0, y = 0, width = self.side, height = self.side, fill = 'white'))
        for place, datum in self.grid.data.items():
            i, j = place
            elements.append(svg.Rect(x = i * block, y = j * block, width = block, height = block, fill = datum.color))
        for ant in self.grid.ants:
            i, j = ant.place
            if ant.datum:
                elements.append(svg.Rect(x = i * block, y = j * block, width = block, height = block, fill = ant.datum.color))
                elements.append(svg.Rect(x = i * block + 1.5, y = j * block + 1.5, width = block - 3, height = block - 3, fill = 'transparent', stroke = 'black', stroke_width = 3))      
            else:
                elements.append(svg.Rect(x = i * block, y = j * block, width = block, height = block, fill = 'black'))
        image = svg.SVG(width = self.side, height = self.side, elements = elements)
        with open('out/H' + str(self.grid.height) + 'W' + str(self.grid.width) + 'C' + str(self.grid.clusters) + 'I' + str(self.grid.iteration) + '.svg', 'w') as file:
            file.write(str(image))