import time

import pygame

from src.colors import *
from src.constants import *


class WormRenderer:
    DEATH_COLORS = [RED, LIGHT_GREY, WHITE, BLUE, BLACK, RED, LIGHT_GREY]

    def __init__(self, screen):
        self.__screen = screen
        self.__color = BLUE

    def render(self, worm, field_x, field_y):
        for x, y in worm.get_body():
            pos_x = x * CELL_SIZE + field_x
            pos_y = y * CELL_SIZE + field_y

            pygame.draw.rect(self.__screen, self.__color, [pos_x, pos_y, CELL_SIZE, CELL_SIZE])

    def death(self, worm, field_x, field_y):
        for color in WormRenderer.DEATH_COLORS:
            time.sleep(0.1)
            self.__color = color
            self.render(worm, field_x, field_y)
            pygame.display.flip()





