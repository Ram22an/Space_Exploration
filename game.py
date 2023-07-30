# sdl=simple directmedia layer
def game():
    import pygame as py
    WIDTH, HEIGHT = 900, 500
    WIN = py.display.set_mode((WIDTH, HEIGHT))
    py.display.set_caption("Space_Exploration")
    RUN = True
    while RUN:
        for event in py.event.get():
            if event.type == py.QUIT:
                RUN = False
    py.quit()
