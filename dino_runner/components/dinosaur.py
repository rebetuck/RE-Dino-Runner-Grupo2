from mimetypes import init
import pygame
from dino_runner.utils.constants import RUNNING

class Dinosaur():
    X_POS = 80
    Y_POS = 310

    def __init__(self) -> None:
        self.latest_image = 0
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        

        # Definiendo la posicion del dino
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

        self.step_index = 0
        

    def update(self):
        pass

    def draw(self, screen):
        """self.current_image += 1
        if self.current_image > 1:
            self.current_image = 0"""
# cambiar el movimiento de la imagen a update
        if int(self.step_index) %2 == 0:
            self.latest_image = 0
        else:
            self.latest_image = 1
        
        self.image = RUNNING[self.latest_image]

        screen.blit(self.image, (self.dino_rect.x,self.dino_rect.y))
        self.increment_index = 0.1
        self.step_index += self.increment_index



    """def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()

        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

        self.step_index += 1
"""