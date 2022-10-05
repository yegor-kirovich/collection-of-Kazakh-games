from Objects.Object import *


class Woman(Object):
    def __init__(self, main_screen, screen_size_x, screen_size_y, pos_x, pos_y):
        super().__init__(main_screen, screen_size_x, screen_size_y)
        self.x = pos_x
        self.y = pos_y
        self.start = True

    def start(self):
        self.start = False
