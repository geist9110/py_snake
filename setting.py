# snake game option
from snake_object import Body

class Setting:
    def __init__(self, background, wall):
        
        ## 게임 반복 ##
        self.running = True
        
        ## 화면 크기 ##
        self.screen_width = wall.width
        self.screen_height = wall.height
        self.title = "Snake for supervised learning"
        
        ## head start location ##
        self.head_start = [5, 5]
        
        ## body object ##
        body1 = Body(self.head_start[0] - 1, self.head_start[1])
        body2 = Body(self.head_start[0] - 2, self.head_start[1], prev_node = body1)
        self.bodies = [body1, body2]
        