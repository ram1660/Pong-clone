from Paddle import Paddle
import pygame

class Player(Paddle):
    OBJECT_NAME = 'player'
    def __init__(self, name, x=0, y=0, width=0, height=0, direction=1, speed=1):
        super(Player, self).__init__(x, y, width, height, direction, speed)
        self.name = name

    def update(self, pygame: pygame):
        return 

    def update(self, pygame):
        pass