# sdl=simple directmedia layer
# Assets/spaceship_yellow.png is equal to os.path.join('Assets','spaceship_yellow.png')
# Assets/spaceship_red.png is equal to os.path.join('Assets','spaceship_red.png')
import pygame as py
import os
BLUE = (0, 191, 255)
WIDTH, HEIGHT = 900, 500
WIN = py.display.set_mode((WIDTH, HEIGHT))
FPS = 100
YELLOW_SPACESHIP = py.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
RED_SPACESHIP = py.image.load(os.path.join('Assets', 'spaceship_red.png'))


def draw_window():
    WIN.fill(BLUE)
    WIN.blit(YELLOW_SPACESHIP, (100, 200))
    WIN.blit(RED_SPACESHIP, (600, 200))
    py.display.update()


def game():
    clock = py.time.Clock()
    py.display.set_caption("Space_Exploration")
    RUN = True
    while RUN:
        clock.tick(FPS)
        for event in py.event.get():
            if event.type == py.QUIT:
                RUN = False
            draw_window()
    py.quit()
