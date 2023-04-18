from calendar import TUESDAY
from pickle import TRUE
import pygame
import os
from time import *
import random

pygame.init()

#--Window--
WIDTH = 1200
HIGHT = 600
WIN = pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("Flappy Iron Man")
BACKGROUND_COLOR = (0,255,255)
FPS = 60
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'background.png')).convert(), (WIN.get_width(), WIN.get_height()))
run_game = True

#--Load Button Images--
resume_img = pygame.image.load('Assets/resumebutton.png').convert_alpha()
newgame_img = pygame.image.load('Assets/newgamebutton.png').convert_alpha()
options_img = pygame.image.load('Assets/optionsbutton.png').convert_alpha()
quit_img = pygame.image.load('Assets/quitbutton.png').convert_alpha()
play_img = pygame.image.load('Assets/playbutton.png').convert_alpha()
exit_img = pygame.image.load('Assets/exitbutton.png').convert_alpha()
scoreboard_img = pygame.image.load('Assets/scorebardbutton.png').convert_alpha()

#Button Class
class Button():
    def __init__(self, x, y, image) -> None:
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self):
        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()
        
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked == False:
                self.clicked = True
                action = True
            
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked = False

        WIN.blit(self.image, (self.rect.x, self.rect.y))
        return action

#Instances of button classes
resume_button = Button(400, 150, resume_img)
newgame_button = Button(400, 220, newgame_img)
options_button = Button(400, 290, options_img)
quit_button = Button(400, 360, quit_img)
play_button = Button(400, 150, play_img)
exit_button = Button(400, 480, exit_img)
scoreboard_button = Button(400, 220, scoreboard_img)

def draw_window():
    global run_game
    WIN.fill(BACKGROUND_COLOR)
    WIN.blit(BACKGROUND_IMAGE,(0,0))
    if play_button.draw():
        pass# HERE WE MUST CONNECT THE FUNCTIONS TO START THE GAME
    if exit_button.draw():
        run_game = False
    pygame.display.update()


def main():
    global Begin_time
    global dangerzone
    global end_game
    global game_paused
    clock = pygame.time.Clock()

    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and not end_game:
                if event.key == pygame.K_SPACE:
                    end_game = False
            else:
                pass
        
        draw_window()#list_of_walls)


        

if __name__ == "__main__":
    main()