import pygame

from Grid import Grid

pygame.init()
side = 500
screen = pygame.display.set_mode((side, side))
pygame.display.set_caption('Antclusterer')
clock = pygame.time.Clock()
running = True
grid = Grid(50, (500, 100))

def draw():
    block = 10
    screen.fill('white')
    for datum in grid.data:
        x, y = datum
        rectangle = pygame.Rect(x * block, y * block, block, block)
        pygame.draw.rect(screen, 'black', rectangle)
    for ant in grid.ants:
        x, y = ant.place
        rectangle = pygame.Rect(x * block, y * block, block, block)
        pygame.draw.rect(screen, 'red', rectangle)
    for x in range(0, side, block):
        for y in range(0, side, block):
            rect = pygame.Rect(x, y, block, block)
            pygame.draw.rect(screen, 'gray', rect, 1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw()
    pygame.display.flip()
    grid.run()
    # clock.tick(60)

pygame.quit()
