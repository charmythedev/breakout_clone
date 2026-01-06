import pygame
from pygame.sprite import collide_rect
import random


class Ball:
    def __init__(self, window):
        self.window = window
        self.x = 150
        self.y = 400
        self.width = 5
        self.height = 5
        self.speed = 6
        self.timer = 0
        self.color = (255,255,255)
        self.superball = False

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.dx = self.speed
        self.dy = -self.speed


    def draw(self):
        pygame.draw.rect(
            self.window,
            self.color,
            self.rect
        )
    def move(self, paddle, bricks):
        if self.superball:
            self.timer -=1
            if self.timer <= 0:

                self.superball = False
                self.color = (255,255,255)

        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.left <= 0 or self.rect.right >= self.window.get_width():
            self.dx *= -1
        if self.rect.top <= 0:
            self.dy *= -1

        if self.rect.colliderect(paddle.rect):
            self.dy *= -1
            self.rect.bottom = paddle.rect.top

        for brick in bricks[:]:
            if self.rect.colliderect(brick.rect):

                if brick.color == brick.colors[0]:
                    bricks[:] = [b for b in bricks if b.color != brick.colors[0]]
                    print("bomb!")

                elif brick.color == brick.colors[1]:
                    print("SUPERBALL")
                    bricks.remove(brick)
                    self.superball = True
                    self.timer = 120
                    self.color = random.choice(brick.colors)


                else:
                    bricks.remove(brick)
                if not self.superball:
                    self.dy *= -1
                    break
