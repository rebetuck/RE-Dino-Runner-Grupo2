from random import random
import pygame
from dino_runner.components.obstacles.obstaculo import Obstacle
import random

class Cactus(Obstacle):
    def __init__(self, image):
        self.gift = False
        self.type = random.randint(0,2)
        super().__init__(image,self.type,self.gift)
        self.rect.y =320