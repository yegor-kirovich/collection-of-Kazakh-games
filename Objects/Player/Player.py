import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, image_idle, image_sit, image_jump):
        pygame.sprite.Sprite.__init__(self)
        self.image_idle = pygame.transform.scale(image_idle, (image_idle.get_width() * 3, image_idle.get_height() * 3))
        self.image_sit = pygame.transform.scale(image_sit, (image_sit.get_width() * 3, image_sit.get_height() * 3))
        self.image_jump = pygame.transform.scale(image_jump, (image_jump.get_width() * 3, image_jump.get_height() * 3))
        self.image = self.image_idle
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 100, 362
        self.spawn_y = 362
        self.distance = 362
        self.jump_distance = 300   #Change
        self.jump, self.sit, self.up = False, False, True
        self.speed = 20

    def default(self):
        self.jump, self.up = False, True
        self.speed, self.rect.y = 20, 362
        self.image = self.image_idle

    def update(self):
        print(self.speed)
        if self.jump:
            if self.up:
                self.image = self.image_jump
                self.distance -= self.speed
                self.rect.y = self.distance
                self.speed -= (2/3)
                if self.rect.y <= self.spawn_y - self.jump_distance:
                    self.up = False
            else:
                self.speed += (2/3)
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
            self.image = self.image_idle
