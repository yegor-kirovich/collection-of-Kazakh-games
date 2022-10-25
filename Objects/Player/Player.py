import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, image_idle, image_sit, image_jump):
        pygame.sprite.Sprite.__init__(self)
        self.image_idle = pygame.transform.scale(image_idle, (image_idle.get_width() * 3, image_idle.get_height() * 3))
        self.image_sit = pygame.transform.scale(image_sit, (image_sit.get_width() * 3, image_sit.get_height() * 3))
        self.image_jump = pygame.transform.scale(image_jump, (image_jump.get_width() / 8.32 * 3, image_jump.get_height() / 7.76 * 3))
        self.image = self.image_idle
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 100, 400
        self.spawn_y = 400
        self.jump_distance = 300    #Change
        self.jump, self.sit, self.up = False, False, True
        self.speed = 20

    def default(self):
        self.jump, self.up = False, True
        self.speed, self.rect.y = 20, 400
        self.image = self.image_idle

    def update(self):
        if self.jump:
            if self.up:
                self.image = self.image_jump
                self.rect.y -= self.speed
                self.speed -= (2/3)
                if self.rect.y <= self.spawn_y - self.jump_distance:
                    self.up = False
            else:
                self.speed += (2/3)
                self.rect.y += self.speed
                if self.rect.y >= self.spawn_y:
                    self.up = True
                    self.jump = False
        elif self.sit:
            if not self.rect.y == self.spawn_y + 69:
                self.rect.y += 69
            self.image = self.image_sit
        elif not self.sit:
            if self.rect.y == self.spawn_y + 69:
                self.rect.y -= 69
            self.image = self.image_idle
