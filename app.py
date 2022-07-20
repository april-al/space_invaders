import pygame

import controls
from gun import Gun
from controls import events_listener
from pygame.sprite import Group

title = 'убийство эдгаров'
bg_color = (0, 0, 0)
screens = (700, 600)


def run():
    pygame.init()
    screen = pygame.display.set_mode(screens)
    pygame.display.set_caption(title)
    gun = Gun(screen)
    bullets = Group()
    while True:
        events_listener(screen, gun, bullets)
        gun.update_gun()
        bullets.update()
        controls.update(bg_color, screen, gun, bullets)


run()
