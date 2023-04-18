import pygame
from time import *
#from adam_Buttons import WIN
import files.variables as variables

class Coins_view():
    def __init__(
        self, 
        x_score = 10,
        y_score = 10

        ) -> None:
        super().__init__()
        self.x_position = x_score
        self.y_position = y_score
        #adam_variables.score_value = 0
        #adam_variables.score = 0
        
        # score Text:
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def show_coins(self):
        #score = self.font.render("Score : " + str(adam_variables.score_value), True, (000,255,255))
        coins = self.font.render("Coins : " + str(variables.coins), True, (000,255,255))
        #WIN.blit(score, (x_score, y_score))
        return coins



        
