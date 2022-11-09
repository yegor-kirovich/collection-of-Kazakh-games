import random
import pygame


class Eagle(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1, 5):
            self.images.append(pygame.image.load("Sprites/Obstacle/eagle_" + str(i) + ".png").convert_alpha())
            self.images[i - 1] = pygame.transform.scale(self.images[i - 1], (self.images[i - 1].get_width() * 4, self.images[i - 1].get_height() * 4))

        self.cur = 0
        self.image = self.images[self.cur]

        self.rect = self.image.get_rect()
        self.rect.x = pos_x

        self.ys = [320, 450, 200]
        self.rect.y = self.ys[random.randint(0, 2)]

    def update(self):
        self.rect.x -= 12
        if self.rect.x <= -100:
            self.kill()

        self.cur += 0.06
        if self.cur >= len(self.images):
            self.cur = 0

        self.image = self.images[int(self.cur)]
