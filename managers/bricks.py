import pygame


class Brick:
    def __init__(self, x, y):
        self.width = 50
        self.height = 20
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def draw(self, window):
        pygame.draw.rect(window, (200, 200, 200), self.rect)
