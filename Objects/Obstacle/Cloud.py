from Objects.Obstacle.Obstacle import *


class Cloud(Obstacle):
    def __init__(self, main_screen, screen_size_x, screen_size_y, x, y, image):
        super().__init__(main_screen, screen_size_x, screen_size_y, x, y)
        self.sprite = pygame.image.load(image)
        self.x = x
        self.y = y

    def move(self):
        if self.is_disable() is False:
            if self.frame != self.time_of_disable:
                if self.frame == 0:
                    self.frame = 2
                else:
                    self.frame += 2
            else:
                self.disable, self.x, self.frame = True, 1300, 0
                self.time_of_disable = self.find_time_of_disable()
        else:
            self.x -= 2

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))
