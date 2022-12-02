from Entity import Entity


class Ball(Entity):
    def __init__(self, x=0, y=0, width=0, height=0, direction=1, speed=1):
        super().__init__(x, y, width, height, direction, speed)

    def update(self, pygame):
        pass

    def __str__(self):
        return 'This is {}. Position: x: {} y: {} speed {}'.format(self.OBJECT_NAME, self.x, self.y, self.speed)
