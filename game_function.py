# snake game function
import pygame

def check_evnets(setting, snake):
    """이벤트에 응답"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            setting.running = False # 파이게임 종료
            print("@", setting.running)
            
        if event.type == pygame.KEYDOWN:
            key_down_events(event, snake)
        
def key_down_events(event, snake):
    if event.key == pygame.K_RIGHT:
        snake.x_pos += 25
        snake.rotated_image = pygame.transform.rotate(snake.image, snake.heading_right)
        
    elif event.key == pygame.K_LEFT:
        snake.x_pos -= 25
        snake.rotated_image = pygame.transform.rotate(snake.image, snake.heading_left)
        
    elif event.key == pygame.K_UP:
        snake.y_pos -= 25
        snake.rotated_image = pygame.transform.rotate(snake.image, snake.heading_up)
        
    elif event.key == pygame.K_DOWN:
        snake.y_pos += 25
        snake.rotated_image = pygame.transform.rotate(snake.image, snake.heading_down)   

def screen_update(screen, background, wall, snake):
    screen.blit(background.image, (background.x_pos, background.y_pos))
    screen.blit(wall.image, (wall.x_pos, wall.y_pos))
    screen.blit(snake.rotated_image, (snake.x_pos, snake.y_pos))
    
    pygame.display.update()