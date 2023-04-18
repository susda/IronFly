import pygame
import os
from time import *
import random
import files.variables as variables

class Background_obj(pygame.sprite.Sprite):
    def __init__(
        self, 
        image_index,
        x_position = 0,
        y_position = 0,
        width=4818, 
        height=600,
        randnum = 0,
        ) -> None:
        super().__init__()
        self.image_index = image_index
        self.randnum = randnum
        self.width = width
        self.height = height
        self.x_position = x_position
        self.y_position = y_position
        self.sprites = []
        images_paths = ['city1.png', 'city2.png', 'city3.png', 'city4.png']
        for i in images_paths:
            self.sprites.append(pygame.image.load(os.path.join('Assets', i))) #8192 × 1024 /1.6 = 4818 x 600
        self.image =  self.sprites[self.image_index]#pygame.transform.scale(self.sprites[self.current_sprite],(self.width, self.height)
        self.rect = self.image.get_rect()
        
        self.rect.topleft = (self.x_position, self.y_position) #sprite
        #
    def move(self):
        if self.rect.x == 0:
            self.add_background()
        if variables.background_can_move:
            self.rect.x -= 2 #to move objects we change rect x and y values

    def add_background(self):
        variables.background_sprite.add(Background_obj(image_index = variables.background_index, x_position=1200))
        if variables.background_index == 3: 
            variables.background_index = 0
        else:
            variables.background_index += 1
        

    def update(self) -> None:
        #variables.can_spawn_background
        self.move()
        if self.rect.x < -1305:
                self.kill()
                variables.can_spawn_background = True #this is kind of bold to do, might be not stable



