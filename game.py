# sdl=simple directmedia layer
# Assets/spaceship_yellow.png is equal to os.path.join('Assets','spaceship_yellow.png')
# Assets/spaceship_red.png is equal to os.path.join('Assets','spaceship_red.png')
import pygame as py
import os

py.font.init()
py.mixer.init()

VEL = 5
BULLET_VEL = 7

WHITE = (255, 255, 255)
REDCO = (255, 0, 0)
YELLOWCO = (255, 255, 0)
BLUE = (0, 191, 255)
BLACK = (0, 0, 0)

YELLOW_HIT = py.USEREVENT + 1
RED_HIT = py.USEREVENT + 2

MAX_BULLETS = 3

BULLET_HIT_SOUND = py.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
BULLET_FIRE = py.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))
WINNER_SOUND = py.mixer.Sound(os.path.join(
    'Assets', 'mixkit-animated-small-group-applause-523.mp3'))

HEALTH_FONT = py.font.SysFont('comicsans', 40)
WINNER_FONT = py.font.SysFont('comicsans', 100)

WIDTH, HEIGHT = 900, 500
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

WIN = py.display.set_mode((WIDTH, HEIGHT))

FPS = 70

BORDER = py.Rect(WIDTH//2, 0, 10, HEIGHT)

YELLOW_SPACESHIP = py.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))

YELLOW_SPACESHIP = py.transform.rotate(py.transform.scale(
    YELLOW_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP = py.image.load(os.path.join('Assets', 'spaceship_red.png'))

RED_SPACESHIP = py.transform.rotate(py.transform.scale(
    RED_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = py.transform.scale(py.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))


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


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH//2-draw_text.get_width() //
             2, HEIGHT//2-draw_text.get_height()//2))
    py.display.update()
    WINNER_SOUND.play()
    py.time.delay(5000)


def draw_window(RED, YELLOW, Red_Bullets, Yellow_Bullets, red_health, yellow_health):
    WIN.fill(BLUE)
    WIN.blit(SPACE, (0, 0))
    py.draw.rect(WIN, BLACK, BORDER)
    red_health_text = HEALTH_FONT.render("Health: "+str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render(
        "Health: "+str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH-red_health_text.get_width()-10, 10))
    WIN.blit(yellow_health_text, (10, 10))
    WIN.blit(YELLOW_SPACESHIP, (YELLOW.x, YELLOW.y))
    WIN.blit(RED_SPACESHIP, (RED.x, RED.y))
    for bullet in Red_Bullets:
        py.draw.rect(WIN, REDCO, bullet)
    for bullet in Yellow_Bullets:
        py.draw.rect(WIN, YELLOWCO, bullet)
    py.display.update()


def game():
    Red_Bullets = []
    Yellow_Bullets = []
    red_health = 10
    yellow_health = 10
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
                if event.key == py.K_LALT and len(Yellow_Bullets) < MAX_BULLETS:
                    bullet = py.Rect(YELLOW.x+YELLOW.width,
                                     YELLOW.y+YELLOW.height//2+4, 10, 5)
                    Yellow_Bullets.append(bullet)
                    BULLET_FIRE.play()

                if event.key == py.K_RALT and len(Red_Bullets) < MAX_BULLETS:
                    bullet = py.Rect(RED.x,
                                     RED.y+RED.height//2+4, 10, 5)
                    Red_Bullets.append(bullet)
                    BULLET_FIRE.play()
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()
        winner_text = ""
        if red_health <= 0:
            winner_text = "YELLOW WINS !!!!"
        if yellow_health <= 0:
            winner_text = "RED WINS !!!!"
        if winner_text != "":
            draw_winner(winner_text)
            break
        KEYS = py.key.get_pressed()
        yellow_movement(KEYS, YELLOW)
        red_movement(KEYS, RED)
        handle_bullets(Yellow_Bullets, Red_Bullets, YELLOW, RED)
        draw_window(RED, YELLOW, Red_Bullets, Yellow_Bullets,
                    red_health, yellow_health)
    py.quit()
