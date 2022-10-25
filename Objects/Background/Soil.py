from Objects.Object import *


class Soil(Object):
    def __init__(self, main_screen, screen_size_x, screen_size_y, image):
        super().__init__(main_screen, screen_size_x, screen_size_y)
        self.sprite = pygame.image.load(image).convert_alpha()
        self.sprite1 = pygame.image.load(image).convert_alpha()
        self.x = 0
        self.x_end = self.sprite.get_width()
        self.y = 500

    def move(self):
        self.x -= 4
        self.x_end -= 4
        if self.x <= -self.sprite.get_width():
            self.x = self.x_end + self.sprite.get_width()
        elif self.x_end <= -self.sprite.get_width():
            self.x_end = self.x + self.sprite.get_width()

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))
        self.screen.blit(self.sprite1, (self.x_end, self.y))
