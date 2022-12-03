from gameObjects.Entity import Entity
import pygame

class Ball(Entity):
    BALL_SIZE = 30
    def __init__(self, surface: pygame.Surface, color: tuple, x=0, y=0, direction=1, speed=1):
        super().__init__(surface, color, x - self.BALL_SIZE // 2, y, self.BALL_SIZE, self.BALL_SIZE, direction, speed)

    def update(self):
        pass


    def render(self) -> None:
        super().render()

    def __str__(self):
        return 'This is {}. Position: x: {} y: {} speed {}'.format(self.OBJECT_NAME, self.x, self.y, self.speed)
