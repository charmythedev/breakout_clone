import pygame
from managers.paddles import Paddle
from managers.ball import Ball
from managers.bricks import Brick
import random

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('comicsans', 20)
font2 = pygame.font.SysFont('comicsans', 50)
lives = 3
timer = 240
COLORS=  [
    (255, 0, 0),     # Red
    (255, 127, 0),   # Orange
    (255, 255, 0),   # Yellow
    (0, 255, 0),     # Green
    (0, 255, 255),   # Cyan
    (0, 0, 255),     # Blue
    (75, 0, 130),    # Indigo
    (148, 0, 211),   # Violet
]

WINDOW = pygame.display.set_mode((500, 700))

FPS = pygame.time.Clock()

player = Paddle(WINDOW)
ball = Ball(WINDOW)

levels = [
    ['XXXXXXXX',
     'XXXXXXXX'],

    ['XXXXXXXX',
     '.XXXXXX.'],

    ['...XX...',
     '..XXXX..',
     '...XX...',
     'XXXXXXXX'],

    ['XXXXXXXXX',
     '.XXXXXXX.',
     '..XXXXX..',
     '...XXX...',
     '....X....'],

     ]
current_level = 0

def build_level(level_layout):
    bricks = []
    gap= 4

    for row in range(len(level_layout)):
        for col in range(len(level_layout[row])):
            if level_layout[row][col] == 'X':
                x = col * (50 + gap) + 35
                y = row * (20 + gap) + 60
                bricks.append(Brick(x, y))

    return bricks

current_level = 0
bricks = build_level(levels[current_level])

running = True
while running:
    FPS.tick(60)
    # 4. Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    player.move(keys)
    ball.move(player, bricks)
    text_surface = font.render(f'lives: {lives}', True, (255, 255, 255))

    WINDOW.fill((0, 0, 0))
    WINDOW.blit(text_surface, (15, 10))
    level_cleared = False
    player.draw()
    ball.draw()
    if ball.superball:
        ball.color = random.choice(COLORS)
    for brick in bricks:
        brick.draw(WINDOW)
    if ball.rect.y > 660:
        lives-=1
        ball.rect.x = 150
        ball.rect.y = 400
        ball.draw()
    if lives <= 0:
        lives = 0
        ball.speed = 0
        ball.dx=0
        ball.dy=0
        game_over_surf = font2.render('GAME OVER', True, (255, 255, 255))
        WINDOW.blit(game_over_surf, (100, 350))
        timer -=1
        if timer <= 0:

            running = False
    if len(bricks) == 0:
        lives += 1
        current_level += 1

        if current_level >= len(levels):
            # player beat the game
            win_surf = font2.render('YOU WIN!', True, (255, 255, 255))
            WINDOW.blit(win_surf, (120, 350))
            pygame.display.update()
            pygame.time.delay(3000)
            running = False
        else:
            bricks = build_level(levels[current_level])

            # FULL ball reset (important)
            ball.rect.center = (250, 500)
            ball.dx = ball.speed
            ball.dy = ball.speed

    pygame.display.update()