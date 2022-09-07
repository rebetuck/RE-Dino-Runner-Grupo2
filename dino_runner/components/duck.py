import pygame
from dino_runner.components.dinosaur import Dinosaur
import random

from dino_runner.utils.constants import DUCKING

class Duck(Dinosaur):
    
    def __init__(self, image):
        super().__init__(image)

        self.image = DUCKING[self.latest_image]
        if int(self.step_index) %2 == 0:
            self.latest_image = 0
        else:
            self.latest_image = 1
        
        self.screen.blit(self.image, (self.dino_rect.x,self.dino_rect.y))
        self.increment_index = 0.1
        self.step_index += self.increment_index
