import pygame, os, random
from snake_object import Snake

class Apple(Snake):
    def __init__ (self, head):
        current_path = os.path.dirname(__file__)
        image_path = os.path.join(current_path, "image")
        self.image = pygame.image.load(os.path.join(image_path, "apple.png"))
        
        self.update_location()
        self.check_location(head)
        self.update_pos()
    
    def update_location(self):
        self.location = [random.randint(1, 20), random.randint(1, 20)]
        
    def check_location(self, head):
        check = head
        while check != None:
            if check.location == self.location:
                self.update_location()
                check = head
            
            else:
                check = check.next