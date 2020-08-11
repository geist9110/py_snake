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
        
        self.location = setting.head_start
        self.update_pos()
        
        self.tail = setting.bodies[-1]
        self.next = setting.bodies[0]
        setting.bodies[0].prev = self
        setting.bodies[0].next = setting.bodies[1]
    
    def head_move(self, event):
        if event.key == pygame.K_RIGHT:
            self.body_move()
            self.location[0] += 1
            self.update_pos()
            self.rotate_head(self.right)
            
        elif event.key == pygame.K_LEFT:
            self.body_move()
            self.location[0] -= 1
            self.update_pos()
            self.rotate_head(self.left)
            
        elif event.key == pygame.K_UP:
            self.body_move()
            self.location[1] -= 1
            self.update_pos()
            self.rotate_head(self.up)
            
        elif event.key == pygame.K_DOWN:
            self.body_move()
            self.location[1] += 1
            self.update_pos()
            self.rotate_head(self.down)
        
    def rotate_head(self, direction):
        self.rotated_image = pygame.transform.rotate(self.image, direction)
        
    def body_move(self):
        self.tail.prev.next = None
        self.next.prev = self.tail
        self.tail = self.tail.prev
        self.next.prev.prev = self
        self.next = self.next.prev
        
        self.next.location = self.location
        self.next.update_pos()
        
class Body(Snake):
    def __init__ (self, x_loc, y_loc, prev_node = None, next_node = None):
        current_path = os.path.dirname(__file__)
        image_path = os.path.join(current_path, "image")
        self.image = pygame.image.load(os.path.join(image_path, "body.png"))
        
        self.next = next_node # next == None : 꼬리 노드
        self.prev = prev_node # 
        
        self.location = [x_loc, y_loc]
        
        self.update_pos()