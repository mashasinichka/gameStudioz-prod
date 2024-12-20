import pygame
import random
import os
from Robot import my_icon

screen_width = 1920
screen_height = 1080
FPS = 60
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_icon(my_icon)
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

