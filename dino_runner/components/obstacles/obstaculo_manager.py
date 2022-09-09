from tkinter import Menu
import pygame
import random
import os
from pygame.locals import * #gestiona eventos
from dino_runner.components.obstacles.obstaculo import Obstacle
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, SOUND_DIR

class Obstacles_manager:

    def __init__(self):
        self.obstacles = []
        self.death_sound = pygame.mixer.Sound(os.path.join(SOUND_DIR,'muerte.mp3'))

    def new_method(self):
        self.game_speed = 15


    def update(self, game):
        self.type_obstacle = [Bird(BIRD), Cactus(LARGE_CACTUS), Cactus(SMALL_CACTUS)]
        if len(self.obstacles) == 0:
            self.obstacles.append(random.choice(self.type_obstacle))

           
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if (game.player.dino_rect.colliderect(obstacle.rect) ):
                if game.player.shield:
                    self.obstacles.pop()
                    break
                if not game.player.has_lives:
                    game.player_heart_manager.reduce_heart_count()
                    if game.player_heart_manager.heart_count > 0:
                        game.player.has_lives = True
                        self.obstacles.pop()
                        start_transition_time = pygame.time.get_ticks()
                        game.player.live_transition_time = start_transition_time + 100
                    else:
                        self.death_sound.play()    
                        pygame.time.delay(500)
                        self.obstacles.remove(obstacle)
                        game.death_count += 1
                        game.playing = False
                        
                        break
                
                
                

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen) 