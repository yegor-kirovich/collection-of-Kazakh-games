import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image_sit = pygame.image.load("Sprites/Player/player_crouch.png").convert_alpha()
        self.image_sit = pygame.transform.scale(self.image_sit,
                                                (self.image_sit.get_width() * 3, self.image_sit.get_height() * 3))

        self.image_jump = pygame.image.load("Sprites/Player/player_jump.png").convert_alpha()
        self.image_jump = pygame.transform.scale(self.image_jump,
                                                 (self.image_jump.get_width() * 3, self.image_jump.get_height() * 3))

        self.images = []
        for i in range(1, 5):
            self.images.append(pygame.image.load("Sprites/Player/player_" + str(i) + ".png").convert_alpha())
            self.images[i - 1] = pygame.transform.scale(self.images[i - 1], (
                self.images[i - 1].get_width() * 3, self.images[i - 1].get_height() * 3))

        self.cur = 0
        self.image = self.images[int(self.cur)]

        self.rect_body = pygame.Rect(127, 362, 60, 100)
        self.rect_horse = pygame.Rect(100, 442, 150, 100)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 100, 362
        self.spawn_y = 362
        self.distance = 362
        self.jump_distance = 300  # Change
        self.jump, self.sit, self.up = False, False, True
        self.speed = 20

    def default(self):
        self.jump, self.sit, self.up = False, False, True
        self.speed, self.rect.y = 20, 362
        self.rect_body.y = 362
        self.distance = 362
        self.image = self.images[int(self.cur)]

    def update(self):
        if self.jump:
            if self.up:
                self.image = self.image_jump
                self.distance -= self.speed
                self.rect.y = self.distance
                self.speed -= (2 / 3)
                if self.rect.y <= self.spawn_y - self.jump_distance:
                    self.up = False
            else:
                self.speed += (2 / 3)
                self.distance += self.speed
                self.rect.y = self.distance
                if self.rect.y >= self.spawn_y:
                    self.up = True
                    self.jump = False
        elif self.sit:
            if not self.rect.y == self.spawn_y + 36:
                self.rect.y += 36
            self.image = self.image_sit
        elif not self.sit:
            if self.rect.y == self.spawn_y + 36:
                self.rect.y -= 36
            self.image = self.images[int(self.cur)]

        self.rect_body.y = self.rect.y
        self.rect_horse.y = self.rect.y + 80

        self.cur += 0.06
        if self.cur >= len(self.images):
            self.cur = 0

        if not self.sit and not self.jump:
            self.image = self.images[int(self.cur)]
