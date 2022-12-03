import sys
import pygame
from gameObjects.ui.divider import Divider
from gameObjects.Player import Player
from gameObjects.Enemy import Enemy
from gameObjects.Ball import Ball
from gameObjects.Entity import Entity


size = width, height = 1280, 720


def init_game_objects(screen: pygame.Surface) -> list[Entity]:
    game_objects = []
    paddle_width, paddle_height = 10, 30
    game_objects.append(Player('Player 1', x=paddle_width, y=height // 2 - paddle_height, width=paddle_width))
    game_objects.append(Enemy(x=width - paddle_width, y=height // 2 - paddle_height, height=paddle_height, width=paddle_width))
    game_objects.append(Divider(width // 2, 0))
    game_objects.append(Ball(width // 2, height // 2))
    return game_objects


def render_ui() -> None:
    pass


def render_game_objects(game_objects: list[Entity]) -> None:
    for game_object in game_objects:
        game_object.render()
    pygame.display.flip()


def update_game_objects(game_objects) -> None:
    for game_object in game_objects:
        game_object.update()


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    game_objects = init_game_objects(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
