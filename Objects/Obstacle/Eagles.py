import pygame


class Eagle(pygame.sprite.Sprite):
    def __init__(self, pos_x, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = 280

    def update(self):
        self.rect.x -= 12
        if self.rect.x <= -100:
            self.kill()
