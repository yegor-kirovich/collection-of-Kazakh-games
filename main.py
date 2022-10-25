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

s_x, s_y = 1200, 700  # width and height of the screen
screen = pygame.display.set_mode((s_x, s_y))  # setting it

condition, frame = "start", 0
speed, space_true = 0, 0

clock = pygame.time.Clock()

start_screen = pygame.font.Font("minecraft.ttf", 42)
text1 = start_screen.render("Press ENTER to start", True, (0, 0, 0, 0.5))

player = Player(screen, s_x, s_y, 100, 370, "sprite#1.png", "abc.png", "sprite_jump.png")
soil = Soil(screen, s_x, s_y, "soil.png")
cloud = Cloud(screen, s_x, s_y, random.randint(0, 1201), 100, "3ZGvh.png")
woman = Woman(screen, s_x, s_y, 900, 370, "kyz.png")


def fill():
    if not objects_obstacles:
        if random.randint(1, 2) == 1:
            objects_obstacles.append(Rock(screen, s_x, s_y, 1500, "Skrytyy-kamen.png"))
        else:
            objects_obstacles.append(Eagle(screen, s_x, s_y, 1500, 280, "ab.png"))
    else:
        if random.randint(1, 2) == 1:
            objects_obstacles.append(Rock(screen, s_x, s_y, objects_obstacles[-1].x + 1100, "Skrytyy-kamen.png"))
        else:
            objects_obstacles.append(Eagle(screen, s_x, s_y, objects_obstacles[-1].x + 1100, 280, "ab.png"))


def delete(i):
    objects_obstacles[i] = None
    objects_obstacles.remove(objects_obstacles[i])


objects, objects_obstacles = [soil, cloud, player], []
stop_queue = False
[fill() for i in range(2)]

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
        [object.draw() for object in objects]
        woman.draw()
        text1 = start_screen.render("Press ENTER to start", True, (0, 0, 0, 0.5))
        screen.blit(text1, (350, 250))
    elif condition == "start-middle":
        frame += 1
        [object.draw() for object in objects]
        woman.start_move()
        woman.draw()
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

        for i, obstacle in zip(range(len(objects_obstacles)), objects_obstacles):
            if not player.sit:
                if player.rect_player.colliderect(obstacle.rect_collision):
                    condition = "game over"
            else:
                pass

            obstacle.move()
            obstacle.draw()
            if obstacle.x < -200:
                fill() if not stop_queue else False
                delete(i)

        if frame >= 120 * 15 and not stop_queue:
            stop_queue = True

        if stop_queue and not objects_obstacles and not player.jump:
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

        for obstacle in objects_obstacles:
            object.draw()
            obstacle.draw()

        if keys[pygame.K_9]:
            player.default()

            condition, frame, objects[1].x = "middle", 0, random.randint(0, 1201)
            while objects_obstacles:
                delete(0)
            [fill() for i in range(2)]
    else:
        text1 = start_screen.render("Victory", True, (0, 0, 0, 0.5))
        screen.blit(text1, (600, 250))
    pygame.display.flip()
