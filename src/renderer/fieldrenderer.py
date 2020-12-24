import pygame
from src.colors import *
from src.constants import *


class FieldRenderer:
    def __init__(self, screen):
        self.__screen = screen

    def render(self, x, y, width, height):

        for i in range(x + CELL_SIZE, x + width, CELL_SIZE):
            pygame.draw.line(self.__screen, LIGHT_GREY, [i, y], [i, y + height])

        for j in range(y + CELL_SIZE, y + height, CELL_SIZE):
            pygame.draw.line(self.__screen, LIGHT_GREY, [x, j], [x + width, j])

        pygame.draw.rect(self.__screen, WHITE, [x, y, width, height], 1)
