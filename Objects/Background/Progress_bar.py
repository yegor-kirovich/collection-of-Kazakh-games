import pygame


class Progress_bar:
    def __init__(self, pos_x, pos_y):
        self.size_x = 0
        self.x, self.y = pos_x, pos_y
        self.percent = 0
        self.rect_bar = pygame.Rect(pos_x, pos_y, self.size_x, 20)
        self.rect_background = pygame.Rect(pos_x - 2, pos_y - 2, 536, 24)
        self.frame = 0

    def update(self):
        self.percent = int(self.size_x/536*100)
        self.size_x += 5/18
        self.rect_bar.update(self.x, self.y, self.size_x, 20)
        print(self.size_x)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect_background)
        pygame.draw.rect(screen, (0, 255, 0), self.rect_bar)
        font = pygame.font.SysFont('minecraft.ttf', 20)
        screen.blit(font.render(f"{self.percent}%", True, (0, 0, 0)), (600, 33))

