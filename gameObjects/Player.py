from gameObjects.Paddle import Paddle
import pygame

class Player(Paddle):
    '''
    Player class
    By default, the player will be always positioned at the left side of the screen.
    Edit the constructor to customize the position.
    '''
    OBJECT_NAME = 'player'
    def __init__(self, name, surface, color, x=0, y=0, width=0, height=0, direction=0, speed=20):
        super(Player, self).__init__(surface, color, x, y, width, height, direction, speed)
        self.name = name

    def update(self) -> None:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.move_up()
            elif event.type == pygame.KEYUP:
                self.move_down()

    def move_up(self) -> None:
        if self._surface.get_height() > self._y - self._speed > 0:
            self._y -= self._speed

    def move_down(self) -> None:
        if self._surface.get_height() > self._y - self._speed > 0:
            self._y += self._speed

    def render(self) -> None:
        return super().render()