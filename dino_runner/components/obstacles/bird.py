import pygame
from dino_runner.components.obstacles.obstaculo import Obstacle
import random

from dino_runner.utils.constants import BIRD

class Bird(Obstacle): 
    def __init__(self, image):
        self.imdex = 0
        self.type = 0
        super().__init__(image,self.type)
        self.rect.y = random.randint(120, 180)
        
        self.image = BIRD
        

    def draw(self, screen):
        self.type = (self.imdex % 10) // 5
        screen.blit(self.image[self.type], self.rect)
        self.imdex += 1

        
        