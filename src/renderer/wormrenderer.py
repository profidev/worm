import pygame

from src.colors import *
from src.constants import *


class WormRenderer:
    def __init__(self, screen):
        self.__screen = screen

    def render(self, worm, field_x, field_y):
        for x, y in worm.get_body():
            pos_x = x * CELL_SIZE + field_x
            pos_y = y * CELL_SIZE + field_y

            print(x, y)
            print(field_x, field_y, pos_x, pos_y)

            pygame.draw.rect(self.__screen, BLUE, [pos_x, pos_y, CELL_SIZE, CELL_SIZE])
