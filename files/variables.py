import pygame

#dangerzone = 9999
#score_value = 0
score = 0
coins = 0
shots = 0
can_call_begin = True 
end_game = True
background_index = 0
can_spawn_background= True
end_time = 0
show_menu = True
#build_menu_once = True
background_can_move = True
wall_score_byID_list = []
laser_shots = 2
show_intro = True
can_restart_intro = True
can_play_endgamesong = True
can_add_game_over_banner = True
#--Objects--

background_sprite = pygame.sprite.Group()
character_sprite = pygame.sprite.Group()
walls_sprite = pygame.sprite.Group()
shots_sprite = pygame.sprite.Group()
coins_sprite = pygame.sprite.Group()
buttons_sprite = pygame.sprite.Group()
game_over_banner_sprite = pygame.sprite.Group()

#-----------
#function
#
function_int = 0 #1 is reset game
#