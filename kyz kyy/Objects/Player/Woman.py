import pygame


class Woman(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.start = True
        self.final = False
        self.frame = 0
        self.woman_speed = 0

        self.images = []
        for i in range(1, 5):
            self.images.append(pygame.image.load("Sprites/MainGoal)/woman_" + str(i) + ".png").convert_alpha())
            self.images[i - 1] = pygame.transform.scale(self.images[i - 1], (
            self.images[i - 1].get_width() * 3, self.images[i - 1].get_height() * 3))

        self.cur = 0
        self.image = self.images[self.cur]

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 900, 388

    def add_speed(self):
        self.woman_speed += 0.25

    def update(self):
        if self.start:
            self.rect.x += 1
            if self.rect.x >= 1200:
                self.start = False
        if self.final:
            self.rect.x -= self.woman_speed

        self.cur += 0.06
        if self.cur >= len(self.images):
            self.cur = 0

        self.image = self.images[int(self.cur)]
