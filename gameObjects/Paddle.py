from gameObjects.Entity import Entity
import pygame
class Paddle(Entity):
    OBJECT_NAME = 'paddle'
    PADDLE_HEIGHT, PADDLE_WIDTH = 100, 30
    def __init__(self, surface: pygame.Surface, color: tuple, x=0, y=0, direction=1, speed=1):
        super().__init__(surface, color, x, y + self.PADDLE_WIDTH, self.PADDLE_WIDTH, self.PADDLE_HEIGHT, direction, speed)
    
    def update(self) -> None:
        pass

    def render(self) -> None:
        return super().render()
