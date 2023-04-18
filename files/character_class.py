import pygame
import os
from time import *
import files.variables as variables
from files.shot_class import Shot
from pygame import mixer

class Character(pygame.sprite.Sprite):
    def __init__(
        self, 
        width=100, 
        height=24, 
        x_position=0, 
        y_position=1, 
    ) -> None:
        super().__init__()
        self.velocity = 0.5
        self.width = width
        self.height = height
        self.sprites = []
        #---
        images_paths = ['iron_man_1.png', 'IronManfiring1.png', 'IronManfiring2.png', 'IronManfiring3.png']#0 = flying, (123)= shooting,...
        for i in images_paths:
            self.sprites.append(pygame.image.load(os.path.join('Assets', i)))#456 × 383 = (76,64)
        self.current_sprite = 0
        self.image = pygame.transform.scale(self.sprites[self.current_sprite],(width,height)) #sprite
        #---
        self.rect = self.image.get_rect() #sprite
        self.rect.topleft = (x_position, y_position) #sprite
        self.scales = [(100,24),(43,75),(44,74),(76,64)]#scales of images
        # Animation booleans
        self.anim_shooting = False
        self.can_shoot = False
        self.anim_jumping = False
        self.can_play_noAmoSound = False
        self.rotation = 0
        self.lasershot_sound = mixer.Sound(os.path.join('Assets/Sounds', 'laser.mp3'))
        self.outammo = mixer.Sound(os.path.join('Assets/Sounds', 'emptygun.mp3'))
        
    def jump(self):
        self.velocity = -8
    
    def top(self):
        if self.rect.y <= 0:
            self.rect.y = 0
    
    def move(self, starting_time):
        if (self.rect.y < 560): # If character is still in frame -> move.
            if (time() - starting_time > 3): # If we are past the first 5 seconds.
                self.velocity += 0.4 # Increasing the falling velocity.
                self.rect.y += self.velocity # Adding the velocity to our position.
        else: 
            if self.velocity < 0:
                self.rect.y += self.velocity # this is so he can jump again after being on the floor
            else:
                pass #self.rect.y = 560
        

    def begin(self):
        if self.rect.x < 150:
            self.rect.x += 1
            self.rect.y += 2
        else:
            variables.can_call_begin = False

    #def collision(self, dangerzone): # use pygame.sprite.collide....
    #    global end_game
    #    top = dangerzone - 60
    #    bot = dangerzone + 60 - 40
    #    if dangerzone != 9999:
    #        if (self.rect.y < top) or (self.rect.y > bot):
    #            end_game = True
    #            print("Game over!")

    def shoot(self):
       # print(self.current_sprite)
        if self.anim_shooting == True:
            self.current_sprite += 0.3
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.anim_shooting = False
            self.image = pygame.transform.scale(self.sprites[int(self.current_sprite)],self.scales[int(self.current_sprite)]) 
            #trying something
            if int(self.current_sprite) == 1:
                self.can_shoot = True
                self.can_play_noAmoSound = True
            if self.current_sprite > 2.5:
                if self.can_shoot:
                    if variables.laser_shots > 0 :
                        variables.laser_shots -= 1
                        variables.shots_sprite.add(Shot(x_position=self.rect.x, y_position=self.rect.y))
                        self.lasershot_sound.set_volume(0.1)
                        self.lasershot_sound.play() 
                        self.can_shoot = False
                    else:
                        if self.can_play_noAmoSound:
                            self.outammo.set_volume(0.1)
                            self.outammo.play()
                            self.can_play_noAmoSound = False
                            print("no amo")
    
    def controls(self, key):
        if key == pygame.K_SPACE:
            self.jump()
        elif key == pygame.K_f:
            self.anim_shooting = True
        #methods
        self.shoot()
        

    def resetAnimations(self):
        self.anim_jumping = False
        self.anim_shooting = False

    def animation(self):
        pass

    def fall(self):
        if (self.rect.y < 600):
            #self.velocity += 0.2 # Increasing the falling velocity.
            self.rect.y += 8    # Adding the velocity to our position.
            self.rect.x +=1
            self.rotation +=20
            self.image = pygame.transform.rotate(pygame.transform.scale(self.sprites[int(self.current_sprite)],self.scales[int(self.current_sprite)]), self.rotation) 
            
       

    def update(self, key, starting_time):
        #self.tick_state += 1
        if not variables.end_game:
            self.move(starting_time) #character.control(0)#passing 0 here (or anything basically) will  reuslt in character falling instead of jumping or doing any action
        #--asking character to check for
            #self.collision(dangerzone)
            if variables.can_call_begin:
                self.begin()
        else:
            self.fall()
        self.controls(key)
        
        
