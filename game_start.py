#######################################
import pygame
from setting import Setting
import game_function as gf
from background import Background, Wall
from snake_object import Head
from apple_object import Apple
#######################################
## 게임 시작 ##
def run_game():
    pygame.init()

    background = Background()
    wall = Wall()
    
    setting = Setting(background, wall)
    
    head = Head(setting)
    
    apple = Apple(head)
    
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    pygame.display.set_caption(setting.title)
        
    while setting.running:
        gf.check_evnets(setting, head, apple)
        gf.screen_update(screen, setting, background, wall, head, apple)
        gf.collide_head_apple(setting, head, apple)
        gf.collide_head_body(setting, head)
    pygame.quit()
#######################################