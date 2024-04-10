import pygame

class Renderer():
    def __init__(self, grid):
        self.grid = grid
        self.side = 1000
        self.screen = pygame.display.set_mode((self.side, self.side))
        self.clock = pygame.time.Clock()

    def draw(self, grid):
        block = self.side // grid.height 
        self.screen.fill('white')
        for place, datum in grid.data.items():
            x, y = place
            rectangle = pygame.Rect(x * block, y * block, block, block)
            pygame.draw.rect(self.screen, datum.color, rectangle)
        for ant in grid.ants:
            x, y = ant.place
            rectangle = pygame.Rect(x * block, y * block, block, block)
            if ant.datum:
                pygame.draw.rect(self.screen, ant.datum.color, rectangle)
                pygame.draw.rect(self.screen, 'black', rectangle, 2)        
            else:
                pygame.draw.rect(self.screen, 'black', rectangle)

    def render(self):
        pygame.init()
        pygame.display.set_caption('Antclusterer')
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw(self.grid)
            pygame.display.flip()
            self.grid.step()
        pygame.quit()