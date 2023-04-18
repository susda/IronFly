from re import I
import pygame
import os
from time import *
import random
import files.variables as variables

class Coin(pygame.sprite.Sprite):
    def __init__(
        self, 
        y_position,
        x_position = 1200,
        width = 40, 
        height = 40
        ) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.x_position = x_position
        self.y_position = y_position
        self.sprites = []
        # images:
        self.images_paths = ['Coin1.png','Coin2.png','Coin3.png','Coin4.png','Coin5.png']
        for i in self.images_paths:
            self.sprites.append(pygame.image.load(os.path.join('Assets', 'Coins', i)))
        self.image_index = 0
        self.image =  pygame.transform.scale(self.sprites[self.image_index],(self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x_position, self.y_position) #sprite position
        

#coins = [pygame.image.load(os.path.join('Assets', 'Coins', 'Coin1.png')), pygame.image.load(os.path.join('Assets', 'Coins', 'Coin2.png')), pygame.image.load(os.path.join('Assets', 'Coins', 'Coin3.png')), pygame.image.load(os.path.join('Assets', 'Coins', 'Coin4.png')), pygame.image.load(os.path.join('Assets', 'Coins', 'Coin5.png')), pygame.image.load(os.path.join('Assets', 'Coins', 'Coin6.png'))]
    def move(self):
        self.rect.x -= 6 #int(6 +(0.1*adam_variables.score))
        if self.rect.x < -30 :
            self.kill()
        
    def update(self) -> None:
        #print(str(self.rect.x) +" <x , y>"+ str(self.rect.y))
        self.move()
        self.image_index += 0.2
        #WIN.blit(self.coin_images[coin_count], (coin_x, self.y_possibility))
        if int(self.image_index) == (len(self.images_paths)-1):
            self.image_index = 0
        #self.image =  pygame.transform.scale(self.sprites[int(self.image_index)],(self.width, self.height))
        self.image =  pygame.transform.scale(self.sprites[int(self.image_index)],(self.width, self.height))
       


        
            

       