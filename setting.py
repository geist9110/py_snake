# snake game option
class Setting:
    def __init__(self, background, wall):
        
        ## 게임 반복 ##
        self.running = True
        
        ## 화면 크기 ##
        self.screen_width = wall.width
        self.screen_height = wall.height
        self.title = "Snake for supervised learning"