import pygame
from dino_runner.components.obstaculo import Obstacle
import random

class Bird(Obstacle): 
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image,self.type)
        self.rect.y =290