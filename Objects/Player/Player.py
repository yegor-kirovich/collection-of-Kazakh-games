from Objects.Object import *


class Player(Object):
    def __init__(self, main_screen, screen_size_x, screen_size_y, x, y, image_idle, image_sit, image_jump):
        super().__init__(main_screen, screen_size_x, screen_size_y)
        self.sprite_idle, self.sprite_sit, self.sprite_jump = pygame.image.load(image_idle).convert_alpha(), pygame.image.load(image_sit).convert_alpha(), pygame.image.load(image_jump).convert_alpha()
        self.sprite_idle = pygame.transform.scale(self.sprite_idle, (self.sprite_idle.get_width() / 6.66 * 3, self.sprite_idle.get_height() / 6.40 * 3))
        self.sprite_sit = pygame.transform.scale(self.sprite_sit, (self.sprite_sit.get_width() * 3, self.sprite_sit.get_height() * 3))
        self.sprite_jump = pygame.transform.scale(self.sprite_jump, (self.sprite_jump.get_width() / 8.32 * 3, self.sprite_jump.get_height() / 7.76 * 3))
        self.sprite = self.sprite_idle
        self.x, self.y = x, y
        self.spawn_y = self.y
        self.jump_distance = 300    #Change
        self.jump, self.sit, self.up = False, False, True
        self.speed = 20
        self.rect_player = pygame.Rect(self.x, self.y, self.sprite_idle.get_width(), self.sprite_idle.get_height())

    def move(self):
        if self.jump:
            if self.up:
                self.sprite = self.sprite_jump
                self.y -= self.speed
                self.rect_player.y = self.y
                self.speed -= (2/3)
                if self.y <= self.spawn_y - self.jump_distance:
                    self.up = False
            else:
                self.speed += (2/3)
                self.y += self.speed
                self.rect_player.y = self.y
                if self.y >= self.spawn_y:
                    self.up = True
                    self.jump = False
        elif self.sit:
            self.sprite = self.sprite_sit
        elif not self.sit:
            self.sprite = self.sprite_idle
        self.rect_player = pygame.Rect(self.x, self.y, self.sprite.get_width() * 0.8, self.sprite.get_height() * 0.8)

    def draw(self):
        # pygame.draw.rect(self.screen, (255, 255, 255), self.rect_player)
        if self.sit:
            self.screen.blit(self.sprite, (self.x, self.y + 69))
        else:
            self.screen.blit(self.sprite, (self.x, self.y))

    def default(self):
        self.sit, self.jump, self.up = False, False, True
        self.speed, self.y, self.rect_player.y = 20, 370, 370
        self.sprite = self.sprite_idle
