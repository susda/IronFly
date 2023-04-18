from distutils.spawn import spawn
import pygame
import os
from time import *
import random
from files.buttons_class import Button
from files.character_class import Character
from files.background import Background_obj
from files.wand_class import Wand
import files.variables as variables
from pygame import mixer
from files.score import score_flppy
from files.shots_score import shots_flppy
from files.coin import Coin
from files.coins_view import Coins_view
from files.pyvidplayer import Video
from files.game_over_banner import GameOverBanner
#from watchpoints import watch
#watch(variables.function_int)
pygame.init()

#--Window--
WIDTH = 1200
HIGHT = 600

WIN = pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("Flappy Iron Man")

#--Variables--
BACKGROUND_COLOR = (0,0,0)#black  #(0,255,255) 
FPS = 60
Begin_time = time()
starting_time = time()
   
ArcadeMusic2 = mixer.Sound(os.path.join('Assets/Sounds', 'GameSongArcade4(Trap).mp3'))
ArcadeMusic2.set_volume(0.12)
click_sound = mixer.Sound(os.path.join('Assets/Sounds', 'clicksoud.mp3')) 
coin_sound = mixer.Sound(os.path.join('Assets/Sounds', 'coinsound.mp3'))
coin_sound.set_volume(0.1)
gameover = mixer.Sound(os.path.join('Assets/Sounds', 'GameOver.mp3'))
crack1_sound = mixer.Sound(os.path.join('Assets/Sounds', 'wallsmash1.mp3'))

IntroMusic = mixer.Sound(os.path.join('Assets/Sounds/IntroSoundPack', 'IntroMusic.mp3'))


puntos = score_flppy()
disparos = shots_flppy()
coins_view = Coins_view()
#UI cordinations
x_score = 10
y_score = 10
x_shots = 1030 
y_shots = 10
x_coins = 530
y_coins = 10
def draw_window():
    WIN.fill(BACKGROUND_COLOR)
    variables.background_sprite.draw(WIN)
    variables.walls_sprite.draw(WIN)
    variables.coins_sprite.draw(WIN)
    variables.character_sprite.draw(WIN)
    variables.shots_sprite.draw(WIN)
    WIN.blit(puntos.show_score(), (x_score, y_score))
    WIN.blit(disparos.show_shots(), (x_shots, y_shots))
    WIN.blit(coins_view.show_coins(), (x_coins, y_coins))
    #puntos.show_score(x_score, y_score)
     
    if variables.show_menu:
        variables.buttons_sprite.draw(WIN)
    variables.game_over_banner_sprite.draw(WIN)
    pygame.display.update()


def game_over():
    if variables.can_add_game_over_banner == True:
        variables.game_over_banner_sprite.add(GameOverBanner())
        variables.can_add_game_over_banner = False
        

def add_coin():
    randnum = random.randint(130,470) #
    chance = random.randint(0,4)#exists or not
    if chance < 3:
        variables.coins_sprite.add(Coin(y_position = randnum)) #top wall, it will automatically add the bot later from insde class

def add_walls():
    randnum = random.randint(130,470) #loch center betwenn y and y value
    id = random.randint(1000,5000)
    variables.walls_sprite.add(Wand(randnum = randnum,  id = id, top = True)) #top wall, it will automatically add the bot later from insde class

def add_background():
    variables.background_sprite.add(Background_obj(variables.background_index))
    variables.can_spawn_background = False
    if variables.background_index == 3: 
        variables.background_index = 0
    else: 
        variables.background_index += 1

def reset():
    #so basically this will work properly after all walls are already gone..
    #variables.build_menu_once = True #!this is probably not a good idea, but dont want to waste time on it
    variables.score = 0
    variables.coins = 0
    variables.shots = 0
    #variables.score_value = 0
    variables.can_call_begin = True 
    variables.can_add_game_over_banner = True
    variables.end_game  = False
    #variables.background_index = 0
    variables.can_spawn_background = True
    variables.show_menu = False
    variables.laser_shots = 2
    for i in variables.character_sprite:
        i.kill()
    for i in variables.walls_sprite:
        i.kill()
    for i in variables.coins_sprite:
        i.kill()
    for i in variables.game_over_banner_sprite:
        i.kill()
    global Begin_time
    global starting_time 

    Begin_time = time()
    starting_time = time()
    variables.character_sprite.add(Character()) 
    pygame.display.flip()
    variables.can_play_endgamesong = True

def build_menu():
    for i in variables.buttons_sprite: #did this because for some reason i get overlapped buttons
        i.kill()
    variables.buttons_sprite.add(Button(image_path='newgamebutton.png', x_position=400, y_position=280, do_function=1))

def main():
    
    build_menu()
    global Begin_time
    global starting_time
    spawn_coin = False
    clock = pygame.time.Clock()    
    add_background() # spawn the first background image
    vid = Video("Assets/introironfly1.mp4")

    def restart_intro():
        if variables.can_restart_intro == True:
            vid.restart()
            variables.can_restart_intro = False

    def gameoversound():
        if variables.can_play_endgamesong == True:
            gameover.set_volume(0.2)
            gameover.play()
            variables.can_play_endgamesong = False

    
    def main_tick():
        variables.character_sprite.update(0,starting_time)# the 0 is for parameter "key" and 0 means nothing pressed
        variables.walls_sprite.update(variables.end_game)
        variables.background_sprite.update()
        variables.buttons_sprite.update()
        variables.shots_sprite.update()
        variables.coins_sprite.update()
        variables.game_over_banner_sprite.update()
        for character in variables.character_sprite:
            if pygame.sprite.spritecollide(character, variables.walls_sprite, False): #!error here
                variables.end_game = True
                variables.end_time = time()
                gameoversound()
                game_over()
            if pygame.sprite.spritecollide(character, variables.coins_sprite, True):
                coin_sound.play()
                variables.coins +=1
                variables.laser_shots +=1
        for wall in variables.walls_sprite:
            if pygame.sprite.spritecollide(wall, variables.shots_sprite, True): 
                wall.damage()
                crack1_sound.set_volume(0.08)
                crack1_sound.play()

        if variables.end_game == True:
            #if time() - variables.end_time > 3:#! menu delay after end game
            variables.show_menu = True
        else:
            variables.show_menu = False
        #do button function
        if variables.show_menu == True and variables.function_int != 0:
            if variables.function_int == 1: #! why is this set to 1 on the second collide
                click_sound.set_volume(0.08)
                click_sound.play()
                variables.function_int = 0
                reset()
                global spawn_coin
                spawn_coin = False
    
    while variables.show_intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                variables.end_game = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        variables.show_intro = False
                    if event.key == pygame.K_r:
                        vid.restart()
            if event.type == pygame.MOUSEBUTTONDOWN:
                        variables.show_intro = False
        restart_intro()
        vid.draw(WIN, (0, 0), force_draw=False)
        IntroMusic.set_volume(0.05)
        IntroMusic.play()
        pygame.display.update()
    IntroMusic.stop()
    ArcadeMusic2.play(-1)
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                variables.end_game = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if not variables.end_game:
                    variables.character_sprite.update(event.key, starting_time)
                else:
                    if event.key == pygame.K_r:
                        pass#reset()
            if variables.show_menu == False and event.type == pygame.MOUSEBUTTONDOWN:
                variables.character_sprite.update(pygame.K_SPACE, starting_time)
            else :
                pass #do nothing for now
        
        if not variables.end_game:
            
            #--adding a wall to the list every 3 seconds--
            if (time() - starting_time > 3):
                if time() - Begin_time > ((1.2) - (0.025 * variables.score)): #editing this will result in change of walls frequency
                    Begin_time = time()
                    if spawn_coin:
                        add_coin()
                        spawn_coin = False
                    else:
                        add_walls()
                        spawn_coin = True
        #Those will always run:       
        main_tick()
        clock.tick(FPS)
        draw_window()     
        
      
        

if __name__ == "__main__":
    main()