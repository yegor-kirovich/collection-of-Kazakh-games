from Objects.Object import *


class Soil(Object):
    def __init__(self, main_screen, screen_size_x, screen_size_y, image):
        super().__init__(main_screen, screen_size_x, screen_size_y)
        self.sprite = pygame.image.load(image)
        self.x = 0
        self.y = 500

    def move(self):
        self.x -= 4
        if self.x == -1200:
            self.x = 0

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))
