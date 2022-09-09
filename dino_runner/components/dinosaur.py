from pygame.sprite import Sprite
import pygame
import os
from dino_runner.utils.constants import DEFAULT_TYPE, JUMPING, RUNNING, DUCKING, SHIELD_TYPE, SOUND_DIR

class Dinosaur(Sprite):

    X_POS = 50
    Y_POS = 300
    Y_POS_DUCK = 325
    JUMP_VEL = 9

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.state = 0
        self.jump_vel = self.JUMP_VEL
        self.has_lives = False
        self.lives_transition_time = 0
        self.music_fondo = pygame.mixer.Sound(os.path.join(SOUND_DIR,'music.mp3'))
        self.setup_state_boolean()

    def setup_state_boolean (self):
        self.has_powerup = False
        self.shield = False
        self.hammer = False
        self.cake = False
        self.show_text = False
        self.shield_time_up = 0

    def update(self, key_in):
        
        if self.state == 0:
            self.run()
        elif self.state == 1:
            self.duck()
        else:
            self.jump()

        if key_in[pygame.K_DOWN]:
            self.state = 1
            self.jump_vel = self.JUMP_VEL
        elif key_in[pygame.K_UP]:
            
            self.state = 2
        elif key_in[pygame.K_9] and self.music_fondo.get_volume() > 0.0:
            self.music_fondo.set_volume(self.music_fondo.set_volume() - 0.01)
        else:
            if self.state != 2:
                self.state = 0

        self.step_index += 1

    def run(self):
        self.image = RUNNING[(self.step_index % 10) // 5]
        self.dino_rect.y = self.Y_POS

    def duck(self):
        self.image = DUCKING[(self.step_index % 10) // 5]
        self.dino_rect.y = self.Y_POS_DUCK

    def jump(self):
        self.image = JUMPING

        self.dino_rect.y -= self.jump_vel * 4
        self.jump_vel -= 1

        if self.jump_vel < -self.JUMP_VEL:
            self.state = 0
            self.dino_rect.y = self.Y_POS
            self.jump_vel = self.JUMP_VEL


    def check_lives(self):
        if self.has_lives:
            transition_time = round(((self.lives_transition_time - pygame.time.get_ticks()) / 1000))
            if transition_time < 0:
                self.has_lives = False

    def check_visibility(self,screen):
        if self.shield:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks()) / 1000,2)
            if (time_to_show >= 0):
                fond = pygame.font.Font('freesansbold.ttf', 18)
                text = fond.render(f"shield enable for {time_to_show}", True, (0,0,0))
                textRect = text.get_rect()
                textRect.center = (500,40)
                screen.blit(text, textRect)
            else:
                self.shield=False
                self.update_to_default(SHIELD_TYPE)

    def update_to_default(self, current_type):
        if(self.type == current_type):
            self.type = DEFAULT_TYPE
            
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        #player.