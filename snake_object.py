import pygame, os

class Snake:
    def update_pos(self):
        self.x_pos = (self.location[0] - 1) * 25 + 1
        self.y_pos = (self.location[1] - 1 )* 25 + 1

class Head(Snake):
    def __init__ (self, setting):
        current_path = os.path.dirname(__file__)
        image_path = os.path.join(current_path, "image")
        self.image = pygame.image.load(os.path.join(image_path, "head.png"))
        
        self.right = 90
        self.up = 180
        self.left = 270
        self.down = 360
        
        self.rotated_image = pygame.transform.rotate(self.image, self.right)
        
        self.location = setting.head_start[:]
        self.update_pos()
        
        self.tail = setting.bodies[1]
        self.last_tail_location = self.tail.location[:]
        
        self.next = setting.bodies[0]
        setting.bodies[0].prev = self
        setting.bodies[0].next = setting.bodies[1]
    
    def head_move(self, setting, event):
        self.last_tail_location = self.tail.location[:]
        self.body_move()
        
        if event.key == pygame.K_RIGHT:
            self.location[0] += 1
            self.rotate_head(self.right)
            
        elif event.key == pygame.K_LEFT:
            self.location[0] -= 1
            self.rotate_head(self.left)
            
        elif event.key == pygame.K_UP:
            self.location[1] -= 1
            self.rotate_head(self.up)
            
        elif event.key == pygame.K_DOWN:
            self.location[1] += 1
            self.rotate_head(self.down)
            
        self.update_pos()
        
    def rotate_head(self, direction):
        self.rotated_image = pygame.transform.rotate(self.image, direction)
        
    def body_move(self):
        self.tail.prev.next = None
        self.next.prev = self.tail
        self.tail = self.tail.prev
        self.next.prev.prev = self
        self.next = self.next.prev
        
        self.next.location = self.location[:]
        self.next.update_pos()
        
class Body(Snake):
    def __init__ (self, location, prev_node = None, next_node = None):
        current_path = os.path.dirname(__file__)
        image_path = os.path.join(current_path, "image")
        self.image = pygame.image.load(os.path.join(image_path, "body.png"))
        
        self.next = next_node
        self.prev = prev_node
        
        self.location = location[:]
        self.update_pos()