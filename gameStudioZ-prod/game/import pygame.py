import pygame
import random
import os

class Platform(pygame.splite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load('platform.jfif').convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


try:
    background = pygame.image.load('back.ipg').convert()
except pygame.error as e:
    print(f"Не удалось загрузить фон")