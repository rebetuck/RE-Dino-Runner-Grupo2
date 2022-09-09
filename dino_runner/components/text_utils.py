import pygame

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_STYLE = 'freesansbold.ttf'
black_color = (0,0,0)

def get_score_element(point):
    font = pygame.font.Font(FONT_STYLE, 30)   
    text = font.render("Points: " + str(point), True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (900,70)

    return text, text_rect

def get_center_message(message, widht=SCREEN_WIDTH //2, height=SCREEN_WIDTH//2):
    font = pygame.font.Font(FONT_STYLE, 70)
    text = font.render(message, True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (widht, height)

    return text, text_rect
