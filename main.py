import pygame
import time
import sys

from Consts import *
from Screen import Screen
from Ball import Ball
from Paddles import Paddles
from Bomb import Bomb
from Star import Star

pygame.init()

game_display = Screen()
ball = Ball()
player_2 = Paddles(pygame.K_UP, pygame.K_DOWN)
player_1 = Paddles(pygame.K_w, pygame.K_s)
last_bomb_spawn_time = time.time()
bomb = Bomb()
last_star_spawn_time = time.time()
star = Star()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        player_1.control(event)
        player_2.control(event)

    game_display.screen.blit(game_display.image, (0, 0))


    game_display.draw(ball, player_1, player_2)
    game_display.game_over(player_1, player_2)

    current_time = time.time()
    if current_time - last_star_spawn_time > star_spawn_interval:
        star_list.append(Star())
        last_star_spawn_time = current_time
    for star in star_list:
        star.draw(game_display.screen)

    if current_time - last_bomb_spawn_time > bomb_spawn_interval:
        bomb_list.append(Bomb())
        last_bomb_spawn_time = current_time
    for bomb in bomb_list:
        bomb.draw(game_display.screen)

    pygame.display.update()