import pygame
import os
from time import *
import random
import files.variables as variables

class Button(pygame.sprite.Sprite):
    def __init__(
        self, 
        image_path,
        #key,
        do_function,
        x_position,
        y_position,
        width = 400, 
        height = 60
        ) -> None:
        super().__init__()
        self.do_function = do_function
        #self.key = key
        self.image_path = image_path
        self.width = width
        self.height = height
        self.x_position = x_position
        self.y_position = y_position
        self.sprites = []
        self.clicked = False
        # images:
        self.sprites.append(pygame.image.load(os.path.join('Assets',image_path))) #.convert())#convert function can lead to transparency issues.
        self.image_index = 0
        self.image =  pygame.transform.scale(self.sprites[self.image_index],(self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x_position, self.y_position) #sprite position
        #self.can_set_function_int = True
        #self.randnum = random.randint(888,9999)
        
    def update(self) -> None:
        if variables.show_menu:
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]==1 and self.clicked == False:
                    self.clicked = True
                    #print("button clicked")
                    variables.function_int = self.do_function            
                if pygame.mouse.get_pressed()[0]==0:
                    self.clicked = False
        #if passed_key == self.key:
        #    self.do_function #pass #here do the action needed
       