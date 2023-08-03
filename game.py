# sdl=simple directmedia layer
# Assets/spaceship_yellow.png is equal to os.path.join('Assets','spaceship_yellow.png')
# Assets/spaceship_red.png is equal to os.path.join('Assets','spaceship_red.png')
import pygame as py
import os
VEL = 5
REDCO = (255, 0, 0)
YELLOWCO = (255, 255, 0)
YELLOW_HIT = py.USEREVENT + 1
RED_HIT = py.USEREVENT + 2
BULLET_VEL = 7
MAX_BULLETS = 3
BLUE = (0, 191, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 900, 500
WIN = py.display.set_mode((WIDTH, HEIGHT))
FPS = 144
BORDER = py.Rect(WIDTH//2, 0, 10, HEIGHT)
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
YELLOW_SPACESHIP = py.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = py.transform.rotate(py.transform.scale(
    YELLOW_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP = py.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = py.transform.rotate(py.transform.scale(
    RED_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = py.transform.scale(py.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))


def draw_window(RED, YELLOW, Red_Bullets, Yellow_Bullets):
    WIN.fill(BLUE)
    WIN.blit(SPACE, (0, 0))
    py.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (YELLOW.x, YELLOW.y))
    WIN.blit(RED_SPACESHIP, (RED.x, RED.y))
    py.display.update()
    for bullet in Red_Bullets:
        py.draw.rect(WIN, REDCO, bullet)
    for bullet in Yellow_Bullets:
        py.draw.rect(WIN, YELLOWCO, bullet)


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


def handle_bullets(Yellow_Bullets, Red_Bullets, YELLOW, RED):
    for bullet in Yellow_Bullets:
        bullet.x += BULLET_VEL
        if RED.colliderect(bullet):
            py.event.post(py.event.Event(RED_HIT))
            Yellow_Bullets.remove(bullet)
        elif bullet.x > WIDTH:
            Yellow_Bullets.remove(bullet)

    for bullet in Red_Bullets:
        bullet.x -= BULLET_VEL
        if YELLOW.colliderect(bullet):
            py.event.post(py.event.Event(YELLOW_HIT))
            Red_Bullets.remove(bullet)
        elif bullet.x < 0:
            Red_Bullets.remove(bullet)


def game():
    Red_Bullets = []
    Yellow_Bullets = []
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
            if event.type == py.KEYDOWN:
                if event.type == py.K_LCTRL and len(Yellow_Bullets) < MAX_BULLETS:
                    bullet = py.Rect(YELLOW.x+YELLOW.width,
                                     YELLOW.y+YELLOW.height//2-2, 10, 5)
                    Yellow_Bullets.append(bullet)

                if event.type == py.K_RCTRL and len(Red_Bullets) < MAX_BULLETS:
                    bullet = py.Rect(RED.x,
                                     RED.y+RED.height//2-2, 10, 5)
                    Red_Bullets.append(bullet)
        handle_bullets(Yellow_Bullets, Red_Bullets, YELLOW, RED)
        KEYS = py.key.get_pressed()
        yellow_movement(KEYS, YELLOW)
        red_movement(KEYS, RED)
        draw_window(RED, YELLOW, Red_Bullets, Yellow_Bullets)
    py.quit()
