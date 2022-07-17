import pygame


class Gun():
    def __init__(self, screen):
        """инициализация шелли"""

        self.screen = screen
        self.image = pygame.image.load('images/canonnnnnn.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def rander(self):
        '''рисование шелли'''
        self.screen.blit(self.image, self.rect)
