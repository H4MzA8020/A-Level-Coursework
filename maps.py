import pygame
from tiles import Tile

pygame.init()

def loadScreen():
    screen = pygame.display.set_mode((1080, 570))
    return screen
#Using linux path system, will not work on Windows.

def loadGrass():
    grass = pygame.image.load("Graphics/grass.png").convert()
    grass = pygame.transform.scale(grass, (216, 114))
    return grass

def loadForest():
    forest = pygame.image.load("Graphics/forest.png").convert()
    forest = pygame.transform.scale(forest, (216, 114))
    return forest

x = 0
y = 0

def Map(screen):
    grass = loadGrass()
    forest = loadForest()
    map = [[Tile(grass, screen).display(x, y), Tile(grass, screen).display(x + 216, y), Tile(grass, screen).display(x + 432, y), Tile(grass, screen).display(x + 648, y), Tile(grass, screen).display(x + 864, y)],
          [Tile(grass, screen).display(x, y+114), Tile(grass, screen).display(x + 216, y+114), Tile(grass, screen).display(x + 432, y+114), Tile(grass, screen).display(x + 648, y+114), Tile(grass, screen).display(x + 864, y + 114)],
          [Tile(grass, screen).display(x, y+228), Tile(grass, screen).display(x + 216, y+228), Tile(grass, screen).display(x + 432, y+228), Tile(grass, screen).display(x + 648, y+228), Tile(grass, screen).display(x + 864, y + 228)],
          [Tile(grass, screen).display(x, y+342), Tile(grass, screen).display(x + 216, y+342), Tile(grass, screen).display(x + 432, y+342), Tile(grass, screen).display(x + 648, y+342), Tile(grass, screen).display(x + 864, y + 342)],
          [Tile(grass, screen).display(x, y+456), Tile(grass, screen).display(x + 216, y+456), Tile(grass, screen).display(x + 432, y+456), Tile(grass, screen).display(x + 648, y+456), Tile(grass, screen).display(x + 864, y + 456)]]

    return map




Map(loadScreen())
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#IMPORTANT: EACH UNIT MUST BE 72x38!!!
