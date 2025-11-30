import pygame
import random
from Consts import *


class Ball:
    def __init__(self):
        self.rect = pygame.Rect(screen_width//2, screen_height//2, ball_size, ball_size)
        self.image = pygame.transform.scale(ball_image, (ball_size, ball_size))
        self.bomb_list = bomb_list
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.last_player_touch = 0
        self.star_list = star_list

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def bounce(self):
        if self.rect.left < 0: self.speed_x *= -1
        if self.rect.right > screen_width: self.speed_x *= -1
        if self.rect.top < 0: self.speed_y *= -1
        if self.rect.bottom > screen_height: self.speed_y *= -1

    def start_position(self):
        self.rect.center = (screen_width//2, screen_height//2)
        self.speed_x = random.choice([-1, 1]) * speed_x
        self.speed_y = random.choice([-1, 1]) * speed_y

    def check_goals(self, player_1, player_2):
        if self.rect.right >= screen_width:
            player_1.score += 1
            self.start_position()

        if self.rect.left <= 0:
            player_2.score += 1
            self.start_position()

        if self.rect.colliderect(player_1.rect1):
            self.speed_x *= -1
            self.last_player_touch = 'player1touch'

        if self.rect.colliderect(player_2.rect2):
            self.speed_x *= -1
            self.last_player_touch = 'player2touch'

    def check_bomb_collisions(self, player_1, player_2):
        for mine in self.bomb_list[:]:
            if self.rect.colliderect(mine.rect):
                self.bomb_list.remove(mine)
                if self.last_player_touch == 'player1touch' :
                    player_2.score += 1
                if self.last_player_touch == 'player2touch' :
                    player_1.score += 1

    def check_star_collisions(self, player_1, player_2):
        for score_booster in self.star_list[:]:
            if self.rect.colliderect(score_booster.rect):
                self.star_list.remove(score_booster)
                if self.last_player_touch == 'player1touch' :
                    player_1.score += 1
                if self.last_player_touch == 'player2touch' :
                    player_2.score += 1

