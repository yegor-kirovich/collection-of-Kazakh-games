import random
import sys

import pygame

#def collided(sprite, other):
#    return sprite.hitbox.colliderect(other.hitbox)
#
#collided_sprites = pygame.sprite.spritecollide(sprite, group, dokill, collided)

from Objects.Obstacle.Rock import *
from Objects.Obstacle.Eagles import *
from Objects.Player.Player import *
from Objects.Background.Soil import *
from Objects.Obstacle.Cloud import *
from Objects.Player.Woman import *
from Objects.Background.Progress_bar import *

pygame.init()

s_x, s_y = 1200, 700  # width and height of the screen
screen = pygame.display.set_mode((s_x, s_y))  # setting it
pygame.display.set_caption("Kyz Kyy")

condition, frame = "start", 0
space_true = 0

clock = pygame.time.Clock()

start_screen = pygame.font.Font("minecraft.ttf", 42)
text1 = start_screen.render("Press ENTER to start", True, (0, 0, 0, 0.5))

player = Player()
soil = Soil(0, screen)
soil_1 = Soil(1200, screen)
cloud = Cloud(random.randint(0, 1201), 100)
woman = Woman()
progress_bar = Progress_bar(350, 30)

players_group = pygame.sprite.Group()
players_group.add(player)

womans_group = pygame.sprite.Group()
womans_group.add(woman)

background_group = pygame.sprite.Group()
background_group.add(soil, soil_1)

cloud_group = pygame.sprite.Group()
cloud_group.add(cloud)


def fill():
    if not obstacles_group:
        if random.randint(1, 2) == 1:
            obstacles_group.add(Rock(1300))
        else:
            obstacles_group.add(Eagle(1300))
    else:
        if random.randint(1, 2) == 1:
            obstacles_group.add(Rock(obstacles_group.sprites()[-1].rect.x + 900))
        else:
            obstacles_group.add(Eagle(obstacles_group.sprites()[-1].rect.x + 900))


def collided1(sprite, other):
    return sprite.rect_horse.colliderect(other.rect)


def collided2(sprite, other):
    return sprite.rect_body.colliderect(other.rect)


obstacles_group = pygame.sprite.Group()
stop_queue = False
[fill() for i in range(2)]

objects = [soil, cloud, player]

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
                woman.add_speed()
                space_true = 0

    screen.fill((27, 235, 250))

    if condition == "start":
        background_group.draw(screen)
        cloud_group.draw(screen)
        players_group.draw(screen)
        womans_group.draw(screen)

        text1 = start_screen.render("Press ENTER to start", True, (0, 0, 0))
        screen.blit(text1, (350, 250))
    elif condition == "start-middle":
        frame += 1

        background_group.draw(screen)
        cloud_group.draw(screen)
        players_group.draw(screen)
        womans_group.draw(screen)

        womans_group.update()

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
        if keys[pygame.K_DOWN] and player.rect.y >= player.spawn_y and not keys[pygame.K_SPACE]:
            player.sit = True
        else:
            player.sit = False

        if pygame.sprite.spritecollideany(player, obstacles_group, collided1):
            condition = "game over"
            continue

        if pygame.sprite.spritecollideany(player, obstacles_group, collided2):
            condition = "game over"
            continue

        progress_bar.draw(screen)
        background_group.draw(screen)
        cloud_group.draw(screen)
        players_group.draw(screen)
        womans_group.draw(screen)
        obstacles_group.draw(screen)

        progress_bar.update()
        cloud_group.update()
        players_group.update()
        background_group.update()
        womans_group.update()
        obstacles_group.update()
        if not stop_queue and len(obstacles_group.sprites()) < 2:
            fill()

        if frame >= 120 * 15 and not stop_queue:
            stop_queue = True

        if stop_queue and len(obstacles_group.sprites()) == 0 and not player.jump:
            condition = "final"
    elif condition == "final":
        player.default()

        text1 = start_screen.render("SPACE", True, (0, 0, 0))
        screen.blit(start_screen.render("SPACE", True, (0, 0, 0)), (600, 250))

        space_true += 1

        if space_true <= 30:
            woman.final = True
            womans_group.update()

        if pygame.sprite.groupcollide(players_group, womans_group, False, False):
            condition = "victory"

        background_group.draw(screen)
        cloud_group.draw(screen)
        players_group.draw(screen)
        womans_group.draw(screen)
    elif condition == "game over":

        background_group.draw(screen)
        cloud_group.draw(screen)
        players_group.draw(screen)
        womans_group.draw(screen)
        obstacles_group.draw(screen)
        progress_bar.draw(screen)

        if keys[pygame.K_9]:
            player.default()
            for obstacle in obstacles_group.sprites():
                obstacle.kill()
            obstacles_group.sprites().clear()
            [fill() for i in range(2)]

            #progress bar
            progress_bar.default()

            condition, frame, cloud_group.sprites()[0] = "middle", 0, random.randint(0, 1200)
    else:
        text1 = start_screen.render("Victory", True, (0, 0, 0, 0.5))
        screen.blit(text1, (520, 250))
    pygame.display.flip()
