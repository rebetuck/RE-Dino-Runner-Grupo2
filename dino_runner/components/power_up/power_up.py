from importlib import import_module
import random
from dino_runner.utils.constants import SCREEN_HEIGHT
from pygame.sprite import Sprite

class PowerUp(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_HEIGHT + random.randint(800, 1200)
        self.rect.x = random.randint(100, 150)
        self.start_time = 0
        self.widht = self.image.get_width()
    
    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed
        if (self.rect.x <-self.rect.width):
            power_ups.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)