import pygame
import random
from dino_runner.components.bird import Bird
from dino_runner.components.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS
from dino_runner.utils.constants import BIRD

class Obstacles_manager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        type_obstacles = [Cactus(SMALL_CACTUS), Bird(BIRD), Cactus(LARGE_CACTUS)]
        if len(self.obstacles) == 0:
            self.obstacles.append(random(len(type_obstacles) ))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if (game.player.dino_rect.colliderect(obstacle.rect) ):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen) 