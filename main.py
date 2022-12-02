import sys, pygame
from gameObjects.Player import Player
from gameObjects.Enemy import Enemy
from gameObjects.Ball import Ball
from gameObjects.Entity import Entity


size = width, height = 1280, 720

def init_game_objects() -> list[Entity]:
    game_objects = []
    game_objects.append(Player())
    game_objects.append(Enemy())
    game_objects.append(Ball())
    return game_objects

def render_ui() -> None:
    pass

def render_game_objects(game_objects) -> None:
    for game_object in game_objects:
        game_object.render()

def update_game_objects(game_objects) -> None:
    for game_object in game_objects:
        game_object.update()

def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    game_objects = init_game_objects()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        


if __name__ == '__main__':
    main()