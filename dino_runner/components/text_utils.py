import pygame

FONT_STYLE = 'freesansbold.ttf'
black_color = (0,0,0)

def get_score_element(point):
    font = pygame.font.Font(FONT_STYLE, 30)   
    text = font.render("Points: " + str(point), True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (900,70)

    return text, text_rect
