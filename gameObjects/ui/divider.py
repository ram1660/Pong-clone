import pygame
class Divider:
    def __init__(self, x, y, screen: pygame.Surface, color: tuple):
        self._x = x
        self._y = y
        self._color = color
        self._screen = screen

    def render(self) -> None:
        starting_y = 0
        for y in range(0, 20, self._screen.get_height()):
            pass