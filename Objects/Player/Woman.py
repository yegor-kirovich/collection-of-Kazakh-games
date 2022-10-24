from Objects.Object import *


class Woman(Object):
    def __init__(self, main_screen, screen_size_x, screen_size_y, pos_x, pos_y, image):
        super().__init__(main_screen, screen_size_x, screen_size_y)
        self.sprite = pygame.image.load(image).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (self.sprite.get_width() / 6.66 * 3, self.sprite.get_height() / 6.40 * 3))
        self.x = pos_x
        self.y = pos_y
        self.start = True
        self.frame = 0
        self.rect_collision = pygame.Rect(self.x, self.y, self.sprite.get_width() * 0.8, self.sprite.get_height() * 0.8)

    def start_move(self):
        self.rect_collision.x = self.x
        self.x += 1
        if self.x >= self.s_x:
            self.start = False

    def last_move(self, speed):
        self.rect_collision.x = self.x
        self.x -= speed

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))