from asyncio import shield
import pygame
import random
from dino_runner.components.power_up.shield import Shield

class PowerUpManager:
    def __init__(self):
        self.powerups = []
        self.when_appears = 0
        self.points = 0
        self.option_number = list(range(1,10))

    def reset_power_ups(self, points):
        self.powerups = []
        self.points = points
        self.when_appears = random.randint(200,300)+self.points

    def generate_power_ups(self, points):
        self.points = points
        if len(self.powerups) == 0:
            if self.when_appears == self.points:
                print("generating powerups")
                self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
                self.powerups.append(Shield())
        return self.powerups

    def update(self, points, game_speed, player):
        self.generate_power_ups(points)
        for powerups in self.powerups:
            powerups.update(game_speed, self.powerups)
            if (player.dino_rect.colliderect(powerups.rect)):
                powerups.star_time = pygame.time.get_ticks()
                player.shield = True
                player.show_text = True
                player.type = powerups.type
                time_random = random.randrange(5,8)
                player.shield_time_up = powerups.start_time + (time_random * 1000)
                self.powerups.remove(powerups)

    def draw(self, screen):
        for powerups in self.powerups:
            powerups.draw(screen)