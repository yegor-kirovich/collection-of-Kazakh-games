import pygame


class Soil(pygame.sprite.Sprite):
    def __init__(self, x, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 525
        self.screen = main_screen

    def update(self):
        self.rect.x -= 4
        if self.rect.x <= -1200:
            self.rect.x = 1200