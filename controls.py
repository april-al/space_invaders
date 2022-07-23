import pygame
import sys
from bullet import Bullet


# def events_listener(screen, gun, bullets):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_d:
#                 gun.move_right = True
#             elif event.key == pygame.K_a:
#                 gun.move_left = True
#             elif event.key == pygame.K_SPACE:
#                 new_bullet = Bullet(screen, gun)
#                 bullets.add(new_bullet)
#         elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_d:
#                 gun.move_right = False
#             elif event.key == pygame.K_a:
#                 gun.move_left = False

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


def update(bg_color, screen, gun, ino, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.rander()
    ino.draw()
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
