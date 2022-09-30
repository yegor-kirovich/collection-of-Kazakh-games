import sys
from Objects.Obstacle.Rock import *
from Objects.Obstacle.Eagles import *

pygame.init()

s_x, s_y = 1200, 800
screen = pygame.display.set_mode((s_x, s_y))


rock = Rock(screen, s_x, s_y, 400, "Skrytyy-kamen.png")
eagle = Eagle(screen, s_x, s_y, 0, 0, "ab.png")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    rock.move()
    eagle.move()

    rock.draw()
    eagle.draw()

    pygame.display.flip()