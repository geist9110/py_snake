import pygame, os

class Head:
    def __init__ (self):
        current_path = os.path.dirname(__file__)
        image_path = os.path.join(current_path, "image")
        self.image = pygame.image.load(os.path.join(image_path, "head.png"))
        
        self.heading_right = 90
        self.heading_up = 180
        self.heading_left = 270
        self.heading_down = 360
        
        self.heading = self.heading_right
        
        self.rotated_image = pygame.transform.rotate(self.image, self.heading)
        
        self.x_pos = 251
        self.y_pos = 251

        
class Body:
    def __init(self):
        pass
