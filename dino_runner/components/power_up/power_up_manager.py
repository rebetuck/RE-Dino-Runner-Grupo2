from asyncio import shield
import os
from pygame.locals import *
from dino_runner.components.power_up.cake import Cake
from dino_runner.components.power_up.hammer import Hammer #gestiona eventos
from dino_runner.utils.constants import SOUND_DIR
import pygame
import random
from dino_runner.components.power_up.shield import Shield

class PowerUpManager:
    def __init__(self):
        self.powerups = []
        self.when_appears = 0
        self.points = 0
        #self.option_number = list(range(1,10))
        self.power_up_sound = pygame.mixer.Sound(os.path.join(SOUND_DIR,'power_up.mp3'))
        self.lives = True

    def reset_power_ups(self, points):
        self.powerups = []
        self.points = points
        self.when_appears = random.randint(300,400)+self.points

    def generate_power_ups(self, points):
        self.points = points
        if len(self.powerups) == 0:
            if self.when_appears == self.points:
                print("generating powerups")
                self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
                self.type_of_power = [Shield(), Cake(), Hammer()]
                self.current_power = random.choice(self.type_of_power)
                self.powerups.append(self.current_power)
        return self.powerups

    def update(self, points, game_speed, player):
        self.generate_power_ups(points)
        for power_up in self.powerups:
            power_up.update(game_speed, self.powerups)
            if (player.dino_rect.colliderect(power_up.rect)):
                power_up.star_time = pygame.time.get_ticks()
                player.shield = True
                player.hammer = True
                player.cake = True
                player.show_text = True
                player.type = power_up.type
                time_random = random.randrange(5,8)
                while player.shield:
                    self.power_up_sound.play()   
                    player.shield_time_up = power_up.start_time + (time_random * 1000)
                    self.powerups.remove(power_up)
                    player.shield = False
                    pygame.mixer.stop()
                    break

    def draw(self, screen):
        for powerup in self.powerups:
            powerup.draw(screen)