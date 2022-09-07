import pygame
from dino_runner.components.obstaculo import Obstacle
import random

from dino_runner.utils.constants import BIRD

class Bird(Obstacle): 
    def __init__(self, image):
        self.type = random.randint(0,1)
        super().__init__(image,self.type)
        self.rect.y =290
        self.index = 0
    
    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image[self.index//5], self.rect)
        self.index += 1
        """

        self.step_index = 0
        if int(self.step_index) %2 == 0:
            self.current_image = 0
        else:
            self.current_image = 1
        
        self.image = BIRD[self.current_image]

        screen.blit(self.image, (self.dino_rect.x,self.dino_rect.y))
        self.increment_index = 0.6
        self.step_index += self.increment_index""" 