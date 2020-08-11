# snake game function
import pygame
from snake_object import Body

def check_evnets(setting, head, apple):
    """이벤트에 응답"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            setting.running = False
            
        if event.type == pygame.KEYDOWN:
            key_down_events(setting, event, head, apple)
        
def key_down_events(setting, event, head, apple):
    head.head_move(setting, event)
        
    if event.key == pygame.K_a:
        apple.update_pos()
        
    if head.x_pos < 1 or head.x_pos > 502 or head.y_pos < 0 or head.y_pos > 502:
        print("game over")
        setting.running = False

def screen_update(screen, setting, background, wall, head, apple):
    screen.blit(background.image, (background.x_pos, background.y_pos))
    screen.blit(wall.image, (wall.x_pos, wall.y_pos))
    screen.blit(head.rotated_image, (head.x_pos, head.y_pos))
    screen.blit(apple.image, (apple.x_pos, apple.y_pos))
    for body in setting.bodies:
        screen.blit(body.image, (body.x_pos, body.y_pos))
    
    pygame.display.update()
    
def collide_head_apple(setting, head, apple):
    
    head_rect = head.image.get_rect()
    head_rect.left = head.x_pos
    head_rect.top = head.y_pos
    
    apple_rect = apple.image.get_rect()
    apple_rect.left = apple.x_pos
    apple_rect.top = apple.y_pos
    
    if head_rect.colliderect(apple_rect):        
        new_body = Body(head.last_tail_location, prev_node = head.tail)
        new_body.update_pos()
        
        head.tail.next = new_body
        head.tail = new_body
        setting.bodies.append(new_body)
        
        apple.update_location()
        apple.check_location(head)
        apple.update_pos()
        
def collide_head_body(setting, head):
    head_rect = head.image.get_rect()
    head_rect.left = head.x_pos
    head_rect.top = head.y_pos
    
    body = head.next
    
    while body != None:
        body_rect = body.image.get_rect()
        body_rect.left = body.x_pos
        body_rect.top = body.y_pos
        
        if head_rect.colliderect(body_rect):
            setting.running = False
            print("Game over")
            break;
            
        else:
            body = body.next
    
    
    