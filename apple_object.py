import pygame, os, random

class Apple:
    def __init__ (self, head):
        current_path = os.path.dirname(__file__)
        image_path = os.path.join(current_path, "image")
        self.image = pygame.image.load(os.path.join(image_path, "apple.png"))
        
        self.x_pos = random.randint(0, 19) * 25 + 1
        self.y_pos = random.randint(0, 19) * 25 + 1
    
    def update_pos(self):
        self.x_pos = random.randint(0, 19) * 25 + 1
        self.y_pos = random.randint(0, 19) * 25 + 1
        
    def update_location(self):
        self.location = [random.randint(1, 20), random.randint(1, 20)]
        
    def check_location(self, head):
        checking = head
        while checking.next == None:
            pass