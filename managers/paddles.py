import pygame


class Paddle:
    def __init__(self, window):

        self.window = window
        self.width = 100
        self.height = 15
        self.speed = 7
        self.x = 200
        self.y = 650

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)



    def draw(self):
        pygame.draw.rect(
            self.window,
            (255, 255, 255),
            self.rect
        )

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 10
        if keys[pygame.K_RIGHT]:
            self.rect.x += 10
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.window.get_width():
            self.rect.right = self.window.get_width()