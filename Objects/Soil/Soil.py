from Objects.Object import *


class Soil(Object):
    def __init__(self, main_screen, screen_size_x, screen_size_y, image):
        super().__init__(main_screen, screen_size_x, screen_size_y)
        self.sprite = pygame.image.load(image)