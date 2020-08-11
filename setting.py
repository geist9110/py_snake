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
        temp1 = self.head_start[:]
        body1 = Body(temp1)
        body1.location[0] -= 1
        body1.update_pos()

        temp2 = self.head_start[:]
        body2 = Body(temp2, prev_node = body1)
        body2.location[0] -= 2
        body2.update_pos()
        
        self.bodies = [body1, body2]