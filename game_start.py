#######################################
import pygame
from setting import Setting
import game_function as gf
from background import Background, Wall
from snake_object import Head
#######################################
## 초기화 ##
pygame.init()

background = Background()
wall = Wall()
snake = Head()

setting = Setting(background, wall)
screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
pygame.display.set_caption(setting.title)

#######################################
## 게임 시작 ##
while setting.running:
    gf.check_evnets(setting, snake)
    gf.screen_update(screen, background, wall, snake)
pygame.quit()
#######################################