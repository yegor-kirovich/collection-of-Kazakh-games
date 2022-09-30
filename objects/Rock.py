import pygame


class Rock:
    def __init__(self, image, pos_y):
        self.sprite = pygame.image.load(image)
        self.x = 0
        self.y = pos_y
        self.disable = False
        self.time_of_disable = self.find_time_of_disable()

    def find_time_of_disable(self) -> int:
        time = random.choice([i for i in range(6)])
        return time

    def is_disable(self) -> bool:
        if self.x >= s_x:
            self.disable = False
        else:
            self.disable = True
        return self.disable

    async def move(self):
        if self.is_disable() is False:
            # delay 1-6
            self.disable, self.x = True, 0
        else:
            self.x += 1

    def draw(self):
        if self.disable:
            screen.blit(self.sprite, (self.x, self.y))