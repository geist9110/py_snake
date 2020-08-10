# snake game function
import pygame

def check_evnets(setting, head, apple):
    """이벤트에 응답"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            setting.running = False
            
        if event.type == pygame.KEYDOWN:
            key_down_events(event, head, apple)
        
def key_down_events(event, head, apple):
    if event.key == pygame.K_RIGHT:
        head.x_pos += 25
        head.rotated_image = pygame.transform.rotate(head.image, head.heading_right)
        
    elif event.key == pygame.K_LEFT:
        head.x_pos -= 25
        head.rotated_image = pygame.transform.rotate(head.image, head.heading_left)
        
    elif event.key == pygame.K_UP:
        head.y_pos -= 25
        head.rotated_image = pygame.transform.rotate(head.image, head.heading_up)
        
    elif event.key == pygame.K_DOWN:
        head.y_pos += 25
        head.rotated_image = pygame.transform.rotate(head.image, head.heading_down) 
        
    if event.key == pygame.K_a:
        apple.update_apple_location()

def screen_update(screen, background, wall, head, apple):
    screen.blit(background.image, (background.x_pos, background.y_pos))
    screen.blit(wall.image, (wall.x_pos, wall.y_pos))
    screen.blit(head.rotated_image, (head.x_pos, head.y_pos))
    screen.blit(apple.image, (apple.x_pos, apple.y_pos))
    
    pygame.display.update()