from Objects.Object import *


class Player(Object):
    def __init__(self, main_screen, screen_size_x, screen_size_y, x, y, image):
        super().__init__(main_screen, screen_size_x, screen_size_y)
        self.sprite = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y
        self.spawn_y = y
        self.jump_distance = 300    #Change
        self.jump = False
        self.sit = False
        self.up = True
        self.speed = 20
        self.i = 0
        self.down = False
        self.rect_player = pygame.Rect(x, y, 250, 166)

    def move(self, image1, image2):
        if self.jump:
            if self.up:
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
        if self.sit:
            self.sprite = pygame.image.load(image1)
        else:
            self.sprite = pygame.image.load(image2)

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect_player)