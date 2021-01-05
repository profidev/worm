import pygame

from src.colors import *


class FieldRenderer:
    def __init__(self, screen):
        self.__screen = screen
        self.__font = pygame.font.SysFont('Impact', 30)

    def render(self, x, y, width, height):
        pygame.draw.rect(self.__screen, LIGHT_GREY, [x, y, width, height])
        pygame.draw.rect(self.__screen, WHITE, [x - 1, y - 1, width + 1, height + 1], 1)

    def write_data(self, score, length, level):
        score_text = self.__font.render('Score: ' + str(score), False, ANTIQUE_WHITE)
        length_text = self.__font.render('Worm length: ' + str(length), False, ANTIQUE_WHITE)
        level_text = self.__font.render('Level: ' + str(level), False, ANTIQUE_WHITE)
        self.__screen.blit(score_text, (110, 30))
        self.__screen.blit(length_text, (310, 30))
        self.__screen.blit(level_text, (590, 30))
