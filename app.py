import pygame

import controls
from constants import screen_size, title, bg_color
from gun import Gun
from controls import events_listener, update_bullets, create_army
from pygame.sprite import Group


def run():
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption(title)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    create_army(screen, inos)

    while True:
        events_listener(screen, gun, bullets)
        gun.update_gun()
        controls.update(bg_color, screen, gun, bullets, inos)
        update_bullets(bullets)
        controls.update_inos(inos)


run()
