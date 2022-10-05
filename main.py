import sys

import pygame

from Objects.Obstacle.Rock import *
from Objects.Obstacle.Eagles import *
from Objects.Player.Player import *
from Objects.Background.Soil import *
from Objects.Obstacle.Cloud import *
from Objects.Player.Woman import *

pygame.init()

s_x, s_y = 1200, 700
screen = pygame.display.set_mode((s_x, s_y))

is_start, frame = 0, 0

clock = pygame.time.Clock()

start_screen = pygame.font.Font(None, 72)
text1 = start_screen.render("Press ENTER to start", True, (0, 0, 0, 0.5))

rock = Rock(screen, s_x, s_y, 1300, "Skrytyy-kamen.png")
eagle = Eagle(screen, s_x, s_y, 1300, 0, "ab.png")
player = Player(screen, s_x, s_y, 0, 250, "abc.png")
soil = Soil(screen, s_x, s_y, "soil.png")
cloud = Cloud(screen, s_x, s_y, 800, 100, "3ZGvh.png")
woman = Woman(screen, s_x, s_y, 700, 250, "kyz.png")


while True:
    clock.tick(120)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and is_start == 0:
                is_start = 1

    screen.fill((27, 235, 250))

    objects = [eagle, soil, rock, cloud, player]

    if is_start == 0:
        soil.draw()
        woman.draw()
        player.draw()
        screen.blit(text1, (350, 250))

    elif is_start == 1:
        frame += 1
        woman.start_a()
        soil.draw()
        woman.draw()
        player.draw()
        if frame <= 120:
            text1 = start_screen.render("1", True, (0, 0, 0, 0.5))
        elif 120 <= frame <= 240:
            text1 = start_screen.render("2", True, (0, 0, 0, 0.5))
        elif 240 <= frame <= 360:
            text1 = start_screen.render("3", True, (0, 0, 0, 0.5))
        if frame == 400:
            is_start = -1
        screen.blit(text1, (600, 250))
    else:
        if keys[pygame.K_SPACE]:
            player.jump = True
        if keys[pygame.K_DOWN] and keys[pygame.K_SPACE] is False:
            player.sit = True
        else:
            player.sit = False

        for object in objects:
            if object == player:
                object.move("123.png", "abc.png")
            else:
                object.move()
            object.draw()

    pygame.display.flip()
