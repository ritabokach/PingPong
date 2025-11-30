import pygame
import sys
from Consts import *
import time

class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.image = pygame.transform.scale(background, (screen_width, screen_height))
        self.caption = pygame.display.set_caption(caption)
        self.font = pygame.font.SysFont('comic sans ms', 120)

    def draw(self, ball, player_1, player_2):
        ball.move()
        ball.draw(self.screen)
        ball.bounce()
        ball.check_bomb_collisions(player_1, player_2)
        ball.check_star_collisions(player_1, player_2)
        ball.check_goals(player_1, player_2)

        player_1.draw_paddle1(self.screen)
        player_2.draw_paddle2(self.screen)
        player_1.move_paddle1()
        player_2.move_paddle2()

        self.show_score(player_1, player_2)


    def show_score(self, player_1, player_2):
        purple = (135, 21, 176)
        player1_score = self.font.render(str(player_1.score), True, purple)
        player2_score = self.font.render(str(player_2.score), True, purple)

        self.screen.blit(player1_score, (screen_width/4, 20))
        self.screen.blit(player2_score, (3 * screen_width / 4, 20))


    def game_over(self, player_1, player_2):
        game_over_text1 = "BLUE PLAYER WON"
        game_over_text2 = "GREEN PLAYER WON"
        green = (59, 150, 117)
        blue = (32, 134, 189)

        if player_1.score == game_over_score or player_2.score == game_over_score:
            pygame.mixer.stop()
            if player_1.score == game_over_score:
                font = pygame.font.SysFont('comic sans ms', 100)
                text_surface = font.render(game_over_text1, True, blue)
                text_rect = text_surface.get_rect()
                text_rect.center = (screen_width//2, screen_height//2)
                self.screen.blit(text_surface, text_rect)
                pygame.display.update()
                pygame.time.wait(2000)
                pygame.quit()
                sys.exit()

            if player_2.score == game_over_score:
                font1 = pygame.font.SysFont('comic sans ms', 100)
                text_surface1 = font1.render(game_over_text2, True, green)
                text_rect1 = text_surface1.get_rect()
                text_rect1.center = (screen_width//2, screen_height//2)
                self.screen.blit(text_surface1, text_rect1)
                pygame.display.update()
                pygame.time.wait(2000)
                pygame.quit()
                sys.exit()




