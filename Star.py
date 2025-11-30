import pygame
import random
from Consts import *

class Star:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(star_size, screen_width-star_size),
                                  random.randint(star_size, screen_height-star_size),
                                  star_size, star_size)
        self.image = pygame.transform.scale(star_image, (star_size, star_size))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
