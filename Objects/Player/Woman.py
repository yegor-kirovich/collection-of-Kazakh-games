from Objects.Object import *


class Woman(Object):
    def __init__(self, main_screen, screen_size_x, screen_size_y, pos_x, pos_y, image):
        super().__init__(main_screen, screen_size_x, screen_size_y)
        self.sprite = pygame.image.load(image)
        self.x = pos_x
        self.y = pos_y
        self.start = True

    def start_move(self):
        self.x += 1
        if self.x >= self.s_x:
            self.start = False

    def last_move(self):
        self.x -= 1

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))