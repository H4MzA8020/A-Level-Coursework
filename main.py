from maps import *
from tiles import *
import pygame

pygame.init()


grass = loadGrass()

forest = loadForest()

Map(loadScreen())

pygame.display.update()
