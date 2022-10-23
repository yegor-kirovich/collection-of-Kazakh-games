from Objects.Obstacle.Obstacle import *


class Cloud(Obstacle):
    def __init__(self, main_screen, screen_size_x, screen_size_y, x, y, image):
        super().__init__(main_screen, screen_size_x, screen_size_y, x, y)
        self.sprite = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y
        self.initial_x = x + 600

    def move(self):
        self.x -= 2
        if self.x <= -300:
            self.x = self.initial_x

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))
