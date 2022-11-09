import pygame


class Rock(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Sprites/Obstacle/stones.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 4, self.image.get_height() * 4))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos_x, 500

    def update(self):
        self.rect.x -= 12
        if self.rect.x <= -100:
            self.kill()
