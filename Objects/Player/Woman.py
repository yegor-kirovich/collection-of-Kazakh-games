import pygame


class Woman(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (image.get_width() * 3, image.get_height() * 3))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 900, 425
        self.start = True
        self.final = False
        self.frame = 0
        self.woman_speed = 0

    def add_speed(self):
        self.woman_speed += 0.25

    def update(self):
        if self.start:
            self.rect.x += 1
            if self.rect.x >= 1200:
                self.start = False
        if self.final:
            self.rect.x -= self.woman_speed
