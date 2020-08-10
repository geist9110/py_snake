# snake game function
import pygame

def event_check(setting):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            setting.running = False