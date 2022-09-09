import pygame
from pygame.locals import * #gestiona eventos
from dino_runner.components.clouds import Clouds
import os
from dino_runner.components.power_up.power_up_manager import PowerUpManager
from dino_runner.components.text_utils import get_center_message
from dino_runner.components.player_hearts.player_heart_manager import PlayerHeartManager
from dino_runner.components import text_utils
from dino_runner.utils.constants import BG, GOV, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, SOUND_DIR
from dino_runner.components.obstacles.obstaculo_manager import Obstacles_manager
from dino_runner.components.dinosaur import Dinosaur


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.points = 0
        self.power_up_manager = PowerUpManager()
        self.running = True
        self.death_count = 0
        self.clouds=Clouds()
        self.player = Dinosaur()
        self.shield = False
        self.obstacle_manager = Obstacles_manager()
        self.player_heart_manager = PlayerHeartManager()
        self.music_fondo = pygame.mixer.Sound(os.path.join(SOUND_DIR,'music.mp3'))
        self.after_death_sound = pygame.mixer.Sound(os.path.join(SOUND_DIR,'after_dead.mp3'))
        
    def run(self):
        # Game loop: events - update - draw
        
        self.music_fondo.play()
        self.create_component()
        self.playing = True
        self.reset()
        self.menu()
        
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
        self.death_count += 1

    def reset(self):
        self.obstacle_manager.obstacles.clear()
        self.playing = True
        self.points = 0
        self.player_heart_manager.draw(self.screen)
        self.power_up_manager.reset_power_ups(0)

    def create_component(self):
        self.power_up_manager.reset_power_ups(self.points)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self,):
        user_imput = pygame.key.get_pressed()
        self.player.update(user_imput)
        self.clouds.update(self.game_speed)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)
        
            

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.clouds.draw(self.screen)
        if self.points > 45:
            self.obstacle_manager.draw(self.screen)
        self.player_heart_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.score()
        self.player.check_lives()
        
        
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def score (self):
        self.points += 1
        score, score_rect = text_utils.get_score_element(self.points)
        if self.points == 7000 or (30000 or 90000):
            self.game_speed += 0.01
        self.player.check_visibility(self.screen)
        self.screen.blit(score, score_rect)

    def menu(self, death_count = 0):
       
        self.running = True
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        self.print_menu_elements(self.death_count)
        
        pygame.display.update()
        
        self.event_to_play()
        
    def print_menu_elements(self, death_count):
        half_screen_height = SCREEN_HEIGHT // 2
        if death_count == 0:
            text, text_rect = text_utils.get_center_message("Press any key to start")
            self.screen.blit(text, text_rect)
            text, text_rect = text_utils.get_center_message("Made by: Rebeca Guerra A.")
            self.screen.blit(text, (120,100))
            self.screen.blit(ICON, (550,300))
        elif death_count > 0:
            self.music_fondo.stop()
            pygame.time.wait(1300)
            self.after_death_sound.play()
            score, score_rect = text_utils.get_center_message("Your score: " + str(self.points), half_screen_height+50)
            text, text_rect = text_utils.get_center_message("Press any key to restart")
            self.screen.blit(score, (120,100))
            self.screen.blit(text, text_rect)
            self.screen.blit(GOV, (550,300))
            pygame.time.wait(1300)
            self.after_death_sound.stop()

 
    def event_to_play(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.run()

            if event.type == pygame.QUIT:
                self.screen.fill((255, 255, 255))
                self.running= False
                self.playing = False 
                pygame.display.quit()
                pygame.quit()
    