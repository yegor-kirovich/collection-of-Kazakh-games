from Objects.Object import *


class Player(Object):
    def __init__(self, main_screen, screen_size_x, screen_size_y, x, y, image):
        super().__init__(main_screen, screen_size_x, screen_size_y)
        self.sprite = pygame.image.load(image)
        self.x = x
        self.y = y
        self.jump = False

    def move(self):
        if self.jump:
            self.y -= 1
            if self.y == 500:
                self.jump = False

        print(self.jump)

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))