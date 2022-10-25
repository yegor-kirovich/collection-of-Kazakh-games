import pygame


class Rock(pygame.sprite.Sprite):
    def __init__(self, pos_x, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (image.get_width() * 4, image.get_height() * 4))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos_x, 500

    def update(self):
        self.rect.x -= 12
        if self.rect.x <= -100:
            self.kill()
