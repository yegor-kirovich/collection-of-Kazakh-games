import pygame


class Cloud(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Sprites/Background/cloud.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= 2
        if self.rect.x <= -300:
            self.rect.x = 1500
