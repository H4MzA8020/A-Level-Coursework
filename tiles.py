import pygame

class Tile:
    def __init__(self, image, screen):
        self.image = image
        self.screen = screen

    def display(self, x, y):
        self.screen.blit(self.image, (x, y))
