import random
import sys

from Objects.Buttons import *

s_x, s_y = 1200, 700
screen = pygame.display.set_mode((s_x, s_y))

buttons_position = [790, 890, 990, 1090]

time, frame = 0, 0

buttons_group = pygame.sprite.Group()

clock = pygame.time.Clock()

while True:
    clock.tick(120)

    time += 1
    frame += 1

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if time == 100 and frame <= 120 * 5:
        choice = random.choice(buttons_position)
        button = Button(choice, buttons_position.index(choice) + 1)
        buttons_group.add(button)
        time = 0
    elif time == 50:
        choice = random.choice(buttons_position)
        button = Button(choice, buttons_position.index(choice) + 1)
        buttons_group.add(button)
        time = 0

    buttons_group.update()
    buttons_group.draw(screen)

    pygame.display.flip()
