import pygame
import os
from time import *
import random
from files.variables import *
from pygame import mixer

class Shot(pygame.sprite.Sprite):
    def __init__(
        self, 
        x_position,
        y_position,
        width = 70, 
        height = 40
        ) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.x_position = x_position
        self.y_position = y_position
        self.sprites = []
        # images:
        self.sprites.append(pygame.image.load(os.path.join('Assets','shot.png'))) #.convert())#convert function can lead to transparency issues.
        self.image_index = 0
        self.image =  pygame.transform.scale(self.sprites[self.image_index],(self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x_position, self.y_position) #sprite position
        self.lasershot_sound = mixer.Sound(os.path.join('Assets/Sounds', 'laser.mp3'))

    def move(self):
        self.rect.x += 12 #to move objects we change rect x and y values
        
    def update(self) -> None:
        self.move()
       