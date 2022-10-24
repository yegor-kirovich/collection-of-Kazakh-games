import random
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
speed, space_true = 0, 0

clock = pygame.time.Clock()

start_screen = pygame.font.Font("minecraft.ttf", 42)
text1 = start_screen.render("Press ENTER to start", True, (0, 0, 0, 0.5))

rock = Rock(screen, s_x, s_y, 1300, "Skrytyy-kamen.png")
eagle = Eagle(screen, s_x, s_y, 2200, 280, "ab.png")
player = Player(screen, s_x, s_y, 100, 370, "sprite#1.png", "abc.png", "sprite_jump.png")
soil = Soil(screen, s_x, s_y, "soil.png")
cloud = Cloud(screen, s_x, s_y, 800, 100, "3ZGvh.png")
woman = Woman(screen, s_x, s_y, 900, 370, "kyz1.png")

objects, objects_obstacles = [soil, cloud, player], [rock, eagle]


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
            if event.key == pygame.K_SPACE and condition == "final":
                speed += 0.25
                space_true = 0

    screen.fill((27, 235, 250))

    if condition == "start":
        soil.draw()
        woman.draw()
        player.draw()
        text1 = start_screen.render("Press ENTER to start", True, (0, 0, 0, 0.5))
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
        if keys[pygame.K_DOWN] and player.y >= player.spawn_y and keys[pygame.K_SPACE] is False:
            player.sit = True
        else:
            player.sit = False

        for object in objects:
            object.move()
            object.draw()

        for i, object in zip(range(len(objects_obstacles)), objects_obstacles):
            if not player.sit:
                if player.rect_player.colliderect(object.rect_collision):
                    condition = "game over"
            else:
                pass

            object.move()
            object.draw()
            if object.x < -50:
                if random.randint(1, 2) == 1:
                    objects_obstacles.append(Rock(screen, s_x, s_y, objects_obstacles[-1].x + 900, "Skrytyy-kamen.png"))
                else:
                    objects_obstacles.append(Eagle(screen, s_x, s_y, objects_obstacles[-1].x + 900, 280, "ab.png"))

                objects_obstacles[i] = None
                objects_obstacles.remove(objects_obstacles[i])

        if frame >= 120 * 15 and not player.jump:
            condition = "final"
    elif condition == "final":
        player.default()

        text1 = start_screen.render("SPACE", True, (0, 0, 0))
        screen.blit(start_screen.render("SPACE", True, (0, 0, 0)), (600, 250))

        space_true += 1

        if space_true <= 30:
            woman.last_move(speed)

        if player.rect_player.colliderect(woman.rect_collision):
            condition = "victory"

        soil.draw()
        woman.draw()
        player.draw()
    elif condition == "game over":
        for object in objects:
            object.draw()

        for object in objects_obstacles:
            object.draw()
    else:
        text1 = start_screen.render("Victory", True, (0, 0, 0, 0.5))
        screen.blit(text1, (600, 250))
    pygame.display.flip()
