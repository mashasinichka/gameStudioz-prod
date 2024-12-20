import pygame
import random
import os
from Robot import screen_height, screen_width

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = screen_height - 300
        self.velocity_y = 0 
        self.on_ground = False
        self.speed = 5 

        def update(self):
            self.rect.y += self.velocity_y
            keys = pygame.Key.get_pressed()
            if keys[pygame.K_a]:
                self.rect.x -= self.speed 
            if kyes[pygame.K_d]:
                self.rect.x += self.speed 
            if self.rect.x < 0:
                self.rect.x = 0
            if self.rect.x > screen_width - self.rect.width:
                self.rect.x = screen_width - self.rect.width

            if not self.on_ground:
                self.velocity_y += 1

        def jump(self):
            if self.on_ground:
                self.velocity_y = -15
        def reset(self):
            self.rect.x = 100
            self.rect.y = screen_height - 150