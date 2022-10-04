from Objects.Object import *


class Player(Object):
    def __init__(self, main_screen, screen_size_x, screen_size_y, x, y, image):
        super().__init__(main_screen, screen_size_x, screen_size_y)
        self.sprite = pygame.image.load(image)
        self.x = x
        self.y = y
        self.spawn_y = y
        self.jump_distance = 300    #Change
        self.jump = False
        self.sit = False
        self.up = True
        self.speed = 20
        self.i = 0

    def move(self, image1, image2):
        if self.jump:
            if self.up:
                self.y -= self.speed
                self.speed -= (2/3)
                if self.y <= self.spawn_y - self.jump_distance:
                    self.up = False
            else:
                self.speed += (2/3)
                self.y += self.speed
                if self.y >= self.spawn_y:
                    self.up = True
                    self.jump = False
            print(self.y)
        if self.sit:
            self.sprite = pygame.image.load(image1)
        else:
            self.sprite = pygame.image.load(image2)

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))
