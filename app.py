import pygame

import controls
from gun import Gun
from controls import events_listener, update_bullets
from pygame.sprite import Group
from ino import Ino

title = 'убийство эдгаров'
bg_color = (0, 0, 0)
screens = (700, 600)


def run():
    pygame.init()
    screen = pygame.display.set_mode(screens)
    pygame.display.set_caption(title)
    gun = Gun(screen)
    ino = Ino(screen)
    bullets = Group()
    while True:
        events_listener(screen, gun, bullets)
        gun.update_gun()
        controls.update(bg_color, screen, gun, ino, bullets)
        update_bullets(bullets)


run()
