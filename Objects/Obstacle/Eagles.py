from Objects.Obstacle.Obstacle import *


class Eagle(Obstacle):
    def __init__(self, main_screen, screen_size_x, screen_size_y, pos_x, pos_y, image):
        super().__init__(main_screen, screen_size_x, screen_size_y, pos_x, pos_y)
        self.sprite = pygame.image.load(image).convert_alpha()
        self.rect_collision = pygame.Rect(self.x, self.y, 150, 150)

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))
        pygame.draw.rect(self.screen, (255, 255, 0), self.rect_collision)
