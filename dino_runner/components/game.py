import imp
import pygame
from dino_runner.components.clouds import Clouds
from dino_runner.components.power_up.power_up_manager import PowerUpManager
from dino_runner.components.text_utils import get_center_message
from dino_runner.components.player_hearts.player_heart_manager import PlayerHeartManager
from dino_runner.components import text_utils
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.obstacles.obstaculo_manager import Obstacles_manager
from dino_runner.components.dinosaur import Dinosaur


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 15
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.points = 0
        self.power_up_manager = PowerUpManager()
        self.running = True
        self.death_count = 0
        self.clouds=Clouds()
        self.player = Dinosaur()
        self.obstacle_manager = Obstacles_manager()
        self.player_heart_manager = PlayerHeartManager()

    def run(self):
        # Game loop: events - update - draw
        self.create_component()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def create_component(self):
        self.power_up_manager.reset_power_ups(self.points)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self,):
        self.player.update(pygame.key.get_pressed())
        self.clouds.update(self.game_speed)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)
        #self.playing = True
        
            

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.clouds.draw(self.screen)
        if self.points > 35:
            self.obstacle_manager.draw(self.screen)
        self.player_heart_manager.draw(self.screen)
        self.score()
        self.player.check_lives()
        self.power_up_manager.draw(self.screen)
        
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
        self.screen.blit(score, score_rect)
        if self.points == 7000 or (30000 or 90000):
            self.game_speed += 0.5
        self.player.check_visibility(self.screen)

    def menu(self):
        self.running = True

        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        self.print_menu_elements("Press any key to start")
        
        pygame.display.update()
        self.event_to_play()
        
    def again(self):
            self.print_menu_elements("Upps you lose, press any key to start again")
            self.event_to_play
            self.screen.blit(self.points, (300, 300))
            self.screen.blit(self.death_count, (500, 500))

    def print_menu_elements(self, text_show):
            text, text_rect = text_utils.get_center_message(text_show)
            self.screen.blit(text, text_rect)

 
    def event_to_play(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running= False
                self.playing = False 
                pygame.display.quit()
                pygame.quit()
                exit()  
            if event.type == pygame.KEYDOWN:
                self.run()
            
