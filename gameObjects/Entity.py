
class Entity:
    OBJECT_NAME = 'entity'

    def __init__(self, x=0, y=0, width=0, height=0, direction=1, speed=1) -> None:
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._direction = direction
        self._speed = speed
    
    def __repr__(self) -> str:
        return 'Entity(x={}, y={}, width={}, height={}, direction={}, speed={})'.format(self.__x, self._y, self._width, self._height, self._direction, self._speed)
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Entity):
            return self.__x == other.__x and self._y == other._y and self._width == other._width and self._height == other._height and self._direction == other._direction and self._speed == other._speed
    
    def __str__(self):
        return 'This is {}. Position: x: {} y: {} speed {}'.format(self.OBJECT_NAME, self.x, self.y, self.speed)