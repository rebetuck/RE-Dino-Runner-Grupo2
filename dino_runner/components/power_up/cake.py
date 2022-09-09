from random import random
import pygame
from dino_runner.components.obstacles.obstaculo import Obstacle
import random

class Cake(Obstacle):
    def __init__(self, image):
        self.type = 0
        self.gift = True
        super().__init__(image,self.type, self.gift)
        self.rect.y =320