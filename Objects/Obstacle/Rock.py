from Objects.Obstacle.Obstacle import *


class Rock(Obstacle):
    def __init__(self, main_screen, screen_size_x, screen_size_y, pos_x, image):
        super().__init__(main_screen, screen_size_x, screen_size_y, pos_x, 600)
        self.sprite = pygame.image.load(image)

    def draw(self):
        if self.disable:
            self.screen.blit(self.sprite, (self.x, self.y))