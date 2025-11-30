import pygame
import random
from Consts import *


class Bomb:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(bomb_size, screen_width-bomb_size),
                                  random.randint(bomb_size, screen_height-bomb_size),
                                  bomb_size, bomb_size)
        self.image = pygame.transform.scale(bomb, (bomb_size, bomb_size))

    def draw(self, screen):
        screen.blit(self.image, self.rect)


