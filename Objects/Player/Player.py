from Objects.Object import *


class Player(Object):
    def __init__(self, main_screen, screen_size_x, screen_size_y, x, y, image):
        super().__init__(main_screen, screen_size_x, screen_size_y)
        self.sprite = pygame.image.load(image)
        self.x = x
        self.y = y
        self.jump = False
        self.up = True

    def move(self):
        if self.jump:
            if self.up:
                self.y -= 0.75
                if self.y == 300:
                    self.up = False
            else:
                self.y += 0.75
                if self.y == 600:
                    self.up = True
                    self.jump = False

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))