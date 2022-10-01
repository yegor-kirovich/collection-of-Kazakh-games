import sys
from Objects.Obstacle.Rock import *
from Objects.Obstacle.Eagles import *
from Objects.Player.Player import *

pygame.init()

s_x, s_y = 1200, 800
screen = pygame.display.set_mode((s_x, s_y))


rock = Rock(screen, s_x, s_y, -600, "Skrytyy-kamen.png")
eagle = Eagle(screen, s_x, s_y, -400, 0, "ab.png")
player = Player(screen, s_x, s_y, 550, 600, "5261963.png")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.jump = True

    screen.fill((0, 0, 0))

    rock.move()
    eagle.move()
    player.move()

    rock.draw()
    eagle.draw()
    player.draw()

    pygame.display.flip()