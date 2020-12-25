import pygame
from src.colors import *
from src.constants import *


class FieldRenderer:
    def __init__(self, screen):
        self.__screen = screen
        self.__font = pygame.font.SysFont('Comic Sans MS', 30)

    def render(self, x, y, width, height):
        pygame.draw.rect(self.__screen, LIGHT_GREY, [x, y, width, height])
        pygame.draw.rect(self.__screen, WHITE, [x - 1, y - 1, width + 1, height + 1], 1)

    def write_data(self, score, length):
        score_text = self.__font.render('Счет: ' + str(score), False, GREEN)
        length_text = self.__font.render('Длинна червяка: ' + str(length), False, GREEN)
        self.__screen.blit(score_text, (130, 10))
        self.__screen.blit(length_text, (410, 10))
