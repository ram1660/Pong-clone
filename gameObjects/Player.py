from gameObjects.Paddle import Paddle
import pygame

class Player(Paddle):
    '''
    Player class
    By default, the player will be always positioned at the left side of the screen.
    Edit the constructor to customize the position.
    '''
    OBJECT_NAME = 'player'
    def __init__(self, name: str, surface: pygame.Surface, color: tuple, x=0, y=0, direction=0, speed=20):
        super(Player, self).__init__(surface, color,super(). PADDLE_WIDTH + x, y, direction, speed)
        self.name = name

    def update(self) -> None:
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
            self.move_up()
        elif pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
            self.move_down()

    def move_up(self) -> None:
        if self._surface.get_height() > self._y - self._speed > 0:
            self._y -= self._speed

    def move_down(self) -> None:
        if self._surface.get_height() > self._y - self._speed > 0:
            self._y += self._speed

    def render(self) -> None:
        return super().render()