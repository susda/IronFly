import pygame
import os
from time import *
import random
import files.variables as variables
from pygame import mixer

class Wand(pygame.sprite.Sprite):
    def __init__(
        self, 
        id,
        top,
        x_position = 1200,
        y_position = 0,
        width=110, 
        height=600,
        wand_choices = [400, 600, 800],
        randnum = 0,
        loch = 182
        ) -> None:
        super().__init__()
        self.id = id # this id is to identify which top and bot are related so the count score once
        self.top = top
        self.randnum = randnum
        self.width = width
        self.height = height
        self.x_position = x_position
        self.y_position = y_position
        self.wand_choices = wand_choices
        #self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.sprites = []
        images_paths = ['wand_blue.png', 'Wand_blue_cracked2.png', 'Wand_blue_cracked2.png']# now index 1 and 2 have same img we used to have heath 3 and 3 states but now only two
        for i in images_paths:
            self.sprites.append(pygame.image.load(os.path.join('Assets',i)))#.convert())#convert function can lead to transparency issues.
        self.current_sprite = 0
        self.image =  pygame.transform.scale(self.sprites[self.current_sprite],(self.width, self.height))
        self.wand_rect_bot = self.image.get_rect()#center=(1200, self.and_height))
        self.wand_rect_top = self.image.get_rect()#center=(1200, self.wand_height - 800))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x_position, self.y_position) #sprite
        self.loch = int(loch- (3 * variables.score)) #make this even numbers better (end result will be this number+1, that 1 is the middle point)
        self.can_add_score = True
        #self.can_add_score_value = True
        self.health = 2
        self.crack1_sound = mixer.Sound(os.path.join('Assets/Sounds', 'wallsmash1.mp3'))
        self.crack2_sound = mixer.Sound(os.path.join('Assets/Sounds', 'wallsmash2.mp3'))
        self.crack2_sound.set_volume(0.1)
        self.crack1_sound.set_volume(0.2)
        self.Playsound = True


        if self.top == False: #is bot
            self.rect.y = self.randnum + int(self.loch/2)
        else: #  is top
            variables.walls_sprite.add(Wand(randnum=randnum, id = self.id, top = False))
            self.image = pygame.transform.rotate(self.image,180)
            self.rect.y = self.randnum - 600 - int(self.loch/2) 

    def move(self):
        self.rect.x -= 6#int(6 +(0.1*variables.score)) #to move objects we change rect x and y values
        
    def damage(self):
        #print("wall took damage")
        self.health -=1

        if self.current_sprite == 1:
            self.crack1_sound.play()
            self.current_sprite =0
        else:
            self.current_sprite += 1
        self.image =  pygame.transform.scale(self.sprites[self.current_sprite],(self.width, self.height))
        

    def update(self,end) -> None:
        #print(self.loch)
        self.move()
        if self.rect.x < -120:
            self.kill()
        if self.health < 1:
            self.kill()


        if (self.rect.x < 90) and (self.can_add_score) and (not end) :#and (self.top): 
            #checking for self.top because we have two walls and we want only one to set score otherwise will add 2 each time
            #print("set can add to false")
            self.can_add_score = False
            #self.can_add_score_value = False
            if self.id in variables.wall_score_byID_list:
                pass # do nothing becase already gained score
            else:
                variables.wall_score_byID_list.clear()
                variables.wall_score_byID_list.append(self.id)
                variables.score = variables.score + 1
                #variables.score_value = variables.score_value +1
                #print(self.font.render("Score :" + str(variables.score_value), True, (255,255,255)))
                if variables.score % 5 == 0:
                    variables.laser_shots += 1
                    print(variables.laser_shots)
                #print(variables.wall_score_byID_list)
                #print("score" + ": " + str(variables.score))
