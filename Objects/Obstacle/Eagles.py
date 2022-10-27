import random
import pygame


class Eagle(pygame.sprite.Sprite):
    def __init__(self, pos_x, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.randik = random.randint(1, 3)
        if self.randik == 1:
            self.rect.y = 220
        elif self.randik == 2:
            self.rect.y = 500
        else:
            self.rect.y = 150

    def update(self):
        self.rect.x -= 12
        if self.rect.x <= -100:
            self.kill()
