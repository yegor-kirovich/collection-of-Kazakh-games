from Objects.Object import *


class Obstacle(Object):
    def __init__(self, main_screen, screen_size_x, screen_size_y, pos_x, pos_y):
        super().__init__(main_screen, screen_size_x, screen_size_y)
        self.x = pos_x
        self.y = pos_y
        self.disable = False
        self.frame = 0
        self.time_of_disable = self.find_time_of_disable()

    def find_time_of_disable(self) -> int:
        time = random.choice([i for i in range(1, 3)])   #Spawn rate should change to make more acceptable game speed
        return time * 120

    def is_disable(self) -> bool:
        if self.x <= -300:
            self.disable = False
        else:
            self.disable = True
        return self.disable

    def move(self):
        if self.is_disable() is False:
            if self.frame != self.time_of_disable:
                if self.frame == 0:
                    self.frame = 1
                else:
                    self.frame += 1
            else:
                self.disable, self.x, self.frame = True, 1300, 0
                self.time_of_disable = self.find_time_of_disable()
        else:
            self.x -= 8
