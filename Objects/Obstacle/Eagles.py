from Objects.Obstacle.Obstacle import *


class Eagle(Obstacle):
    def __init__(self, main_screen, screen_size_x, screen_size_y, pos_x, pos_y, image):
        super().__init__(main_screen, screen_size_x, screen_size_y, pos_x, pos_y)
        self.sprite = pygame.image.load(image).convert_alpha()

    def find_time_of_disable(self):
        time = random.choice([i for i in range(100, 150)])
        return time * 60

    def draw(self):
        if self.disable:
            self.screen.blit(self.sprite, (self.x, self.y))
