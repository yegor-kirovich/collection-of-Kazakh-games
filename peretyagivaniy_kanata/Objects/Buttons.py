import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, x, num):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f"Sprites/button_{num}.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, 0
        self.speed = 2

    def update(self):
        self.speed += 0.0005
        self.rect.y += self.speed
        if self.rect.y >= 700:
            self.kill()
