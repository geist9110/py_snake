#######################################
import pygame
from setting import Setting
from game_function import *
#######################################
## 초기화 ##
pygame.init()

setting = Setting()

#######################################
## 게임 시작 ##
def start(setting):
    while setting.running:
        event_check(setting)
        
        
#######################################

start(setting)