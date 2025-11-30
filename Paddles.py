import pygame
from Consts import *

class Paddles:
    def __init__(self, key_up, key_down):
        self.rect1 = pygame.Rect(0, screen_height//2, paddle_width, paddle_height)
        self.image1 = pygame.transform.scale(paddle_1, (paddle_width, paddle_height))
        self.rect2 = pygame.Rect(screen_width - paddle_width, screen_height // 2, paddle_width, paddle_height)
        self.image2 = pygame.transform.scale(paddle_2, (paddle_width, paddle_height))
        self.key_up = key_up
        self.key_down = key_down
        self.score = 0
        self.speed_y = 0

    def draw_paddle1(self, screen):
        screen.blit(self.image1, self.rect1)

    def draw_paddle2(self, screen):
        screen.blit(self.image2, self.rect2)

    def move_paddle1(self):
        self.rect1.y += self.speed_y
        if self.rect1.top < 0: self.rect1.top = 0
        if self.rect1.bottom > screen_height: self.rect1.bottom = screen_height

    def move_paddle2(self):
        self.rect2.y += self.speed_y
        if self.rect2.top < 0: self.rect2.top = 0
        if self.rect2.bottom > screen_height: self.rect2.bottom = screen_height

    def control(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.key_up:
                self.speed_y = -1 * paddle_speed

            if event.key == self.key_down:
                self.speed_y = paddle_speed

        if event.type == pygame.KEYUP:
            if event.key == self.key_up or event.key == self.key_down:
                self.speed_y = 0