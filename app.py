import pygame
import sys
from gun import Gun

title = 'убийство эдгаров'
colorbg = (0, 0, 0)
screens = (1000, 600)


def run():
    pygame.init()
    screen = pygame.display.set_mode((screens))
    pygame.display.set_caption(title)
    gun = Gun(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(colorbg)
        gun.rander()
        pygame.display.flip()


run()
