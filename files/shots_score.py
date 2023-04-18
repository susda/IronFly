import pygame
from time import *
#from adam_Buttons import WIN
import files.variables as variables

class shots_flppy():
    def __init__(
        self, 
        x_shots = 1000,
        y_shots = 10

        ) -> None:
        super().__init__()
        self.x_position = x_shots
        self.y_position = y_shots
        #adam_variables.score_value = 0
        #adam_variables.score = 0
        
        # score Text:
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def show_shots(self):
        #score = self.font.render("Score : " + str(adam_variables.score_value), True, (000,255,255))
        shots = self.font.render("Shots : " + str(variables.laser_shots), True, (000,255,255))
        #WIN.blit(score, (x_score, y_score))
        return shots