import pygame

screen_width = 1280
screen_height = 720
background = pygame.image.load('images/pong_field.png')
ball_image = pygame.image.load('images/ball.png')
ball_size = 70
bomb = pygame.image.load('images/bomb.png')
bomb_size = 80
paddle_1 = pygame.image.load('images/paddle_1.png')
paddle_2 = pygame.image.load('images/paddle_2.png')
paddle_width = 130
paddle_height = 130
caption = 'PING PONG'
speed_x = 7
speed_y = 5
paddle_speed = 12
game_over_score = 20
game_over_image = pygame.image.load('images/game_over_image.png')
game_over_image_size = 500
bomb_spawn_interval = 3
bomb_list = []
star_image = pygame.image.load('images/star.png')
star_size = 80
star_list = []
star_spawn_interval = 5
