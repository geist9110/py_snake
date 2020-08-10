import pygame, os

class Background:
    def __init__ (self, x_pos = 1, y_pos = 1):
        current_path = os.path.dirname(__file__)
        image_path = os.path.join(current_path, "image")
        
        self.image = pygame.image.load(os.path.join(image_path, "background.png"))
        
        self.size = self.image.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        
        self.x_pos = x_pos
        self.y_pos = y_pos
        
class Wall:
    def __init__ (self, x_pos = 0, y_pos = 0):
        current_path = os.path.dirname(__file__)
        image_path = os.path.join(current_path, "image")
        
        self.image = pygame.image.load(os.path.join(image_path, "wall.png"))
        
        self.size = self.image.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        
        self.x_pos = x_pos
        self.y_pos = y_pos