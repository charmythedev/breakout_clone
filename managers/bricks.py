import pygame
import random


class Brick:
    def __init__(self, x, y):
        self.width = 50
        self.height = 20
        self.colors =[(255, 18, 0),
                      (167, 34, 156),
                      (0, 141, 213),
                      (238,180,179),
                      (78,83,64)

        ]
        self.color = random.choice(self.colors)
        self.rect = pygame.Rect(x, y, self.width, self.height)


    def draw(self, window):
        pygame.draw.rect(window,self.color, self.rect)
