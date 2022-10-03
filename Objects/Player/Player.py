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
        self.up = True

    def move(self):
        if self.jump:
            if self.up:
                self.y -= 10
                if self.y == self.spawn_y - self.jump_distance:
                    self.up = False
            else:
                self.y += 15
                if self.y == self.spawn_y:
                    self.up = True
                    self.jump = False

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))
