import pygame

import controls
from gun import Gun
from controls import events_listener, update_bullets, create_army
from pygame.sprite import Group

title = 'убийство эдгаров'
bg_color = (0, 0, 0)
screen_h = 700
screen_w = 600
screens = (screen_h, screen_w)


def run():
    pygame.init()
    screen = pygame.display.set_mode(screens)
    pygame.display.set_caption(title)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()

    while True:
        events_listener(screen, gun, bullets)
        gun.update_gun()
        controls.update(bg_color, screen, gun, bullets, inos)
        create_army(screen, inos)
        update_bullets(bullets)


run()
