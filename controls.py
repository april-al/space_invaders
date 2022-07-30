import pygame
import sys


from bullet import Bullet
from ino import Ino
from constants import screen_w, screen_h
import time


def events_listener(screen, gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if is_right_key(event):
                gun.move_right = True
            elif is_left_key(event):
                gun.move_left = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if is_right_key(event):
                gun.move_right = False
            elif is_left_key(event):
                gun.move_left = False


def is_right_key(event):
    return event.key == pygame.K_d or event.key == pygame.K_RIGHT


def is_left_key(event):
    return event.key == pygame.K_a or event.key == pygame.K_LEFT


def update(bg_color, screen, gun, bullets, inos):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.rander()
    inos.draw(screen)
    pygame.display.flip()


def update_bullets(screen, inos, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if len(inos) == 0:
        bullets.empty()
        create_army(screen , inos)


def gun_kill(stats, screen, gun, inos, bullets):
    stats.gun_left -= 1
    inos.empty()
    bullets.empty()
    create_army(screen, inos)
    create_army(screen, inos)
    time.sleep(2)


def update_inos(stats, screen, gun, inos, bullets):
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, gun, inos, bullets)
    inos_check(stats, screen, gun, inos, bullets)


def inos_check(stats, screen, gun, inos, bullets):
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, gun, inos, bullets)
            break


def create_army(screen, inos):
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((screen_w - 2 * ino_width) / ino_width)

    ino_height = ino.rect.height
    number_ino_y = int((screen_h - 100 - 2 * ino_height) / ino_height)

    for r in range(1, number_ino_y):
        for n in range(1, number_ino_x + 1):
            ino = Ino(screen)
            ino.x = n * ino_width
            ino.rect.x = ino.x
            ino.y = r * ino_height
            ino.rect.y = ino.y

            inos.add(ino)
