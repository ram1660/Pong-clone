from Entity import Entity
class Paddle(Entity):
    OBJECT_NAME = 'paddle'
    def __init__(self, x=0, y=0, width=0, height=0, direction=1, speed=1):
        super().__init__(x, y, width, height, direction, speed)
    
    def update(self, pygame):
    pass