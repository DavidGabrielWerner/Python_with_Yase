import time

import pygame
from math import pi
import pygame.gfxdraw
import sys


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Game Window
pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tiky Taky")
clock = pygame.time.Clock()

x = 1
y = 1
player_width = 70
player_height = 70
player_x = screen_width // 2 - player_width // 2
player_y = screen_height // 2 - player_height // 2
player_speed = 80

count = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x-30 > 0 and x > 0:
        player_x -= player_speed
        time.sleep(0.1)
        x -= 1
        print(player_x, player_y)
    if keys[pygame.K_RIGHT] and player_x+30 < screen_width - player_width and x < 2:
        player_x += player_speed
        time.sleep(0.1)
        x += 1
        print(player_x, player_y)
    if keys[pygame.K_UP] and player_y-30 > 0 and y > 0:
        player_y -= player_speed
        time.sleep(0.1)
        y -= 1
        print(player_x, player_y)
    if keys[pygame.K_DOWN] and player_y+30 < screen_width - player_width and y < 2:
        player_y += player_speed
        time.sleep(0.1)
        y += 1
        print(player_x, player_y, "y:" + str(y))
    if keys[pygame.K_SPACE]:
        if count%2 == 0:
            print("ghjkl")
            pygame.draw.line(screen, (0, 0, 0), (215,215), (215+70, 215+70), 2)
            pygame.draw.line(screen, (0, 0, 0), (215+70, 215), (215, 215+70), 2)
            time.sleep(0.1)
            count += 1
        else:
            pygame.draw.arc(screen, "blue", [210, 75, 150, 125], pi, 3 * pi / 2, 2)
            time.sleep(0.1)
            count += 1



    clock.tick(60)
    screen.fill((0, 191, 255))

    pygame.draw.line(screen, (0,0,0), (210, 100),(210, 400), 2)
    pygame.draw.line(screen, (0, 0, 0), (290, 100), (290, 400), 2)
    pygame.draw.line(screen, (0, 0, 0), (100, 210), (400, 210), 2)
    pygame.draw.line(screen, (0, 0, 0), (100, 290), (400, 290), 2)

    pygame.gfxdraw.box(screen, (player_x, player_y, player_width, player_height), (255,193,193,50))
    for i in range(2):
        pygame.draw.rect(screen, (0, 0, 0), (player_x - i, player_y - i, player_width, player_height), 1)

    pygame.display.flip()
