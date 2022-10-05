import sys
from Objects.Obstacle.Rock import *
from Objects.Obstacle.Eagles import *
from Objects.Player.Player import *
from Objects.Background.Soil import *
from Objects.Obstacle.Cloud import *

pygame.init()

s_x, s_y = 1200, 700
screen = pygame.display.set_mode((s_x, s_y))

clock = pygame.time.Clock()

rock = Rock(screen, s_x, s_y, 1300, "Skrytyy-kamen.png")
eagle = Eagle(screen, s_x, s_y, 1300, 0, "ab.png")
player = Player(screen, s_x, s_y, 150, 250, "abc.png")
soil = Soil(screen, s_x, s_y, "soil.png")
cloud = Cloud(screen, s_x, s_y, 800, 100, "3ZGvh.png")


while True:
    clock.tick(120)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        player.jump = True
    if keys[pygame.K_DOWN] and keys[pygame.K_SPACE] is False:
        player.sit = True
    else:
        player.sit = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((27, 235, 250))

    objects = [eagle, soil, rock, cloud, player]

    for object in objects:
        if object == player:
            object.move("123.png", "abc.png")
        else:
            object.move()
        object.draw()

    pygame.display.flip()
