# sdl=simple directmedia layer
# Assets/spaceship_yellow.png is equal to os.path.join('Assets','spaceship_yellow.png')
# Assets/spaceship_red.png is equal to os.path.join('Assets','spaceship_red.png')
import pygame as py
import os
VEL = 5
BLUE = (0, 191, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 900, 500
WIN = py.display.set_mode((WIDTH, HEIGHT))
FPS = 100
BORDER = py.Rect(WIDTH/2, 0, 10, HEIGHT)
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
YELLOW_SPACESHIP = py.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = py.transform.rotate(py.transform.scale(
    YELLOW_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP = py.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = py.transform.rotate(py.transform.scale(
    RED_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


def draw_window(RED, YELLOW):
    WIN.fill(BLUE)
    py.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (YELLOW.x, YELLOW.y))
    WIN.blit(RED_SPACESHIP, (RED.x, RED.y))
    py.display.update()


def yellow_movement(KEYS, YELLOW):

    # movement of spaceships with arrow keys and WASD respectively
    if KEYS[py.K_a] and YELLOW.x - VEL > 0:  # LEFT
        YELLOW.x -= VEL
    elif KEYS[py.K_d] and YELLOW.x + YELLOW.width + VEL < BORDER.x:  # RIGHT
        YELLOW.x += VEL
    elif KEYS[py.K_w] and YELLOW.y - VEL > 0:  # UP
        YELLOW.y -= VEL
    elif KEYS[py.K_s] and YELLOW.y + VEL + YELLOW.height < HEIGHT - 10:  # DOWN
        YELLOW.y += VEL
    return YELLOW


def red_movement(KEYS, RED):
    # movement of spaceships with arrow keys and WASD respectively
    if KEYS[py.K_UP] and RED.y - VEL > 0:
        RED.y -= VEL
    elif KEYS[py.K_DOWN] and RED.y + VEL + RED.height < HEIGHT-10:
        RED.y += VEL
    elif KEYS[py.K_RIGHT] and RED.x + RED.width + VEL < WIDTH:
        RED.x += VEL
    elif KEYS[py.K_LEFT] and RED.x - VEL > BORDER.x + BORDER.width:
        RED.x -= VEL
    return RED


def game():
    RED = py.Rect(600, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    YELLOW = py.Rect(100, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = py.time.Clock()
    py.display.set_caption("Space_Exploration")
    RUN = True
    while RUN:
        clock.tick(FPS)
        for event in py.event.get():
            if event.type == py.QUIT:
                RUN = False
        KEYS = py.key.get_pressed()
        yellow_movement(KEYS, YELLOW)
        red_movement(KEYS, RED)
        draw_window(RED, YELLOW)
    py.quit()
