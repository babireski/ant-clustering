import pygame

import Body
import Grid
import Item
import Reader

file = 'inp/C04.txt'
# file = 'inp/C15.txt'
colormap = None
clusters = 4
data = Reader.Reader(file, Item.Item, colormap, clusters, normalize = True).data
# data = [Body.Body() for _ in range(500)]
size = (50, 50)
population = 50
iterations = 1000000

grid = Grid.Grid(size, population, data, iterations, clusters, plots = [0, 200000, 400000, 600000, 800000, 1000000])
grid.run()