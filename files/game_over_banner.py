import pygame
import os
from time import *
import random
from files.variables import *

class GameOverBanner(pygame.sprite.Sprite):
    def __init__(
        self, 
        x_position= 600,
        y_position = 200,
        width = 1200, 
        height = 600
        ) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.x_position = x_position
        self.y_position = y_position
        self.sprites = []
        # images:
        self.sprites.append(pygame.image.load(os.path.join('Assets','Game Over Foto.png'))) #.convert())#convert function can lead to transparency issues.
        self.image_index = 0
        self.image =  pygame.transform.scale(self.sprites[self.image_index],(self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_position, self.y_position) #sprite position
        self.build_time = time()

    def move(self):
        #print(time() - self.build_time)
        
        if time() - self.build_time < 2 :
            #print("first move")
            #self.width = self.width * 0.995
            #self.height = self.height * 0.995
            self.rect.y = self.rect.y * 0.8 #to move objects we change rect x and y values
            self.rect.x = self.rect.x * 1.05
        elif time() - self.build_time > 2.5 :
            #print("second move")
            #self.rect.y = self.rect.y * 1.1 + 1 #to move objects we change rect x and y values
            self.rect.x = self.rect.x * 1.3 + 1
        #print(self.rect.y)
        self.image =  pygame.transform.scale(self.sprites[self.image_index],(self.width, self.height))
        
    def update(self) -> None:
        if self.rect.y > 700 or self.rect.y < -700 or self.rect.x > 1500 or self.rect.x < -1000:
            self.kill()
        self.move()
       