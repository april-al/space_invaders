import pygame
from gun import Gun
from controls import events_listener

title = 'убийство эдгаров'
bg_color = (0, 0, 0)
screens = (700, 600)


def run():
    pygame.init()
    screen = pygame.display.set_mode(screens)
    pygame.display.set_caption(title)
    gun = Gun(screen)
    while True:
        events_listener(gun)
        gun.update_gun()
        screen.fill(bg_color)
        gun.rander()
        pygame.display.flip()


run()
