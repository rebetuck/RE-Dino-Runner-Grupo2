import pygame
import random
from dino_runner.components.obstacles.obstaculo import Obstacle
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class Obstacles_manager:

    def __init__(self):
        self.obstacles = []

    def new_method(self):
        self.game_speed = 15


    def update(self, game):
        self.type_obstacle = [Bird(BIRD), Cactus(LARGE_CACTUS), Cactus(SMALL_CACTUS)]
        if len(self.obstacles) == 0:
            self.obstacles.append(random.choice(self.type_obstacle))

           
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if (game.player.dino_rect.colliderect(obstacle.rect) ):
                if not game.player.has_lives:
                    #pygame.time.delay(500)

                    game.player_heart_manager.reduce_heart_count()
                    if game.player_heart_manager.heart_count > 0:
                        game.player.has_lives = True
                        self.obstacles.pop()
                        start_transition_time = pygame.time.get_ticks()
                        game.player.live_transition_time = start_transition_time + 1000
                    else:    
                        pygame.time.delay(500)
                        self.obstacles.remove(obstacle)
                        game.playing = False
                        game.death_count += 1
                        game.again()
                        break
                
                
                

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen) 