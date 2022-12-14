from gameObjects.Paddle import Paddle
import pygame
class Enemy(Paddle):
    OBJECT_NAME = 'enemy'
    def __init__(self, surface: pygame.Surface, color: tuple, x=0, y=0, direction=1, speed=1):
        super().__init__(surface, color, x - (super().PADDLE_WIDTH * 2), y, direction, speed)
    
    def update(self):
        pass
    
    def __str__(self):
        return 'This is {}. Position: x: {} y: {} speed {}'.format(self.OBJECT_NAME, self.x, self.y, self.speed)