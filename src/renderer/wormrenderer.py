import time

import pygame

from src.colors import *
from src.constants import *
from src.worm import Direction


class WormRenderer:
    DEATH_COLORS = [RED, LIGHT_GREY, WHITE, BLUE, BLACK, RED, LIGHT_GREY]

    def __init__(self, screen):
        self.__screen = screen
        self.__color = BLUE

    def render(self, worm, field_x, field_y):
        self.__render_body(field_x, field_y, worm)
        # pygame.mixer.Sound.play(pygame.mixer.Sound("src/renderer/sounds/movement.wav"))

    def __render_body(self, field_x, field_y, worm):
        for i, body_cell in enumerate(worm.get_body()):
            x, y = body_cell
            pos_x = x * CELL_SIZE + field_x
            pos_y = y * CELL_SIZE + field_y

            if i == 0:
                half_ceil = CELL_SIZE / 2
                pygame.draw.circle(self.__screen, self.__color, (pos_x + half_ceil, pos_y + half_ceil), half_ceil)
                if worm.get_direction() == Direction.UP:
                    pygame.draw.rect(
                        self.__screen,
                        self.__color,
                        [pos_x, pos_y + half_ceil, CELL_SIZE, CELL_SIZE]
                    )
                elif worm.get_direction() == Direction.DOWN:
                    pygame.draw.rect(
                        self.__screen,
                        self.__color,
                        [pos_x, pos_y, CELL_SIZE, CELL_SIZE - half_ceil]
                    )
                elif worm.get_direction() == Direction.LEFT:
                    pygame.draw.rect(
                        self.__screen,
                        self.__color,
                        [pos_x + half_ceil, pos_y, CELL_SIZE, CELL_SIZE]
                    )
                elif worm.get_direction() == Direction.RIGHT:
                    pygame.draw.rect(
                        self.__screen,
                        self.__color,
                        [pos_x, pos_y, CELL_SIZE - half_ceil, CELL_SIZE]
                    )
            else:
                pygame.draw.rect(self.__screen, self.__color, [pos_x, pos_y, CELL_SIZE, CELL_SIZE])

    def death(self, worm, field_x, field_y):
        for color in WormRenderer.DEATH_COLORS:
            time.sleep(0.1)
            self.__color = color
            self.__render_body(field_x, field_y, worm)
            pygame.display.flip()





