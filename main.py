import sys

import pygame

from Objects.Obstacle.Rock import *
from Objects.Obstacle.Eagles import *
from Objects.Player.Player import *
from Objects.Background.Soil import *
from Objects.Obstacle.Cloud import *
from Objects.Player.Woman import *

pygame.init()

s_x, s_y = 1200, 700 #width and height of the screen
screen = pygame.display.set_mode((s_x, s_y)) #setting it

condition, frame = "start", 0

clock = pygame.time.Clock()

start_screen = pygame.font.Font("minecraft.ttf", 42)
text1 = start_screen.render("Press ENTER to start", True, (0, 0, 0, 0.5))

rock = Rock(screen, s_x, s_y, 1300, "Skrytyy-kamen.png")
eagle = Eagle(screen, s_x, s_y, 1300, 330, "ab.png")
player = Player(screen, s_x, s_y, 100, 430, "abc.png")
soil = Soil(screen, s_x, s_y, "soil.png")
cloud = Cloud(screen, s_x, s_y, 800, 100, "3ZGvh.png")
woman = Woman(screen, s_x, s_y, 700, 250, "kyz.png")

objects = [soil, rock, cloud, player, eagle]

while True:
    clock.tick(120)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and condition == "start":
                condition = "start-middle"

    screen.fill((27, 235, 250))

    if condition == "start":
        soil.draw()
        woman.draw()
        player.draw()
        screen.blit(text1, (350, 250))
    elif condition == "start-middle":
        frame += 1
        woman.start_move()
        soil.draw()
        woman.draw()
        player.draw()
        if frame <= 120:
            text1 = start_screen.render("1", True, (0, 0, 0, 0.5))
        elif frame <= 240:
            text1 = start_screen.render("2", True, (0, 0, 0, 0.5))
        elif frame <= 360:
            text1 = start_screen.render("3", True, (0, 0, 0, 0.5))
        if frame == 400:
            condition = "middle"
            frame = 0
        screen.blit(text1, (600, 250))
    elif condition == "middle":
        frame += 1
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
        #if frame == 120:
        #    condition = "middle-final"
    elif condition == "middle-final":
        text1 = start_screen.render("SPACE", True, (0, 0, 0, 0.5))
        screen.blit(text1, (600, 250))
        soil.draw()
        woman.draw()
        woman.last_move()
        player.draw()
    else:
        text1 = start_screen.render("Victory", True, (0, 0, 0, 0.5))
        screen.blit(text1, (600, 250))
    pygame.display.flip()
