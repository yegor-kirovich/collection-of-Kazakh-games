import pygame
import sys
import random

pygame.init()

s_x, s_y = 1200, 800
screen = pygame.display.set_mode((s_x, s_y))


class Rock:
    def __init__(self, image, pos_y):
        self.sprite = pygame.image.load(image)
        self.x = 0
        self.y = pos_y
        self.disable = False
        self.frame = 0
        self.time_of_disable = self.find_time_of_disable()

    def find_time_of_disable(self) -> int:
        time = random.choice([i for i in range(50, 100)])
        return time * 60

    def is_disable(self) -> bool:
        if self.x >= s_x:
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
                self.disable, self.x, self.frame = True, 0, 0
                self.time_of_disable = self.find_time_of_disable()
        else:
            self.x += 1

    def draw(self):
        if self.disable:
            screen.blit(self.sprite, (self.x, self.y))


rock = Rock("Skrytyy-kamen.png", 400)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    rock.move()

    rock.draw()

    pygame.display.flip()