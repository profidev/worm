import pygame

from src.constants import *
from src.renderer.fieldrenderer import FieldRenderer
from src.renderer.wormrenderer import WormRenderer
from src.worm import Worm


class Field:

    def __init__(self, screen, level_manager):
        size_x, size_y = pygame.display.get_window_size()
        self.__field_width = FIELD_WIDTH * CELL_SIZE
        self.__field_height = FIELD_HEIGHT * CELL_SIZE
        self.__field_x = round((size_x - self.__field_width) / 2)
        self.__field_y = size_y - self.__field_x - self.__field_height

        self.__field_renderer = FieldRenderer(screen)
        self.__worm = Worm(*level_manager.get_current_level_config())
        self.__worm_renderer = WormRenderer(screen)

    def action(self):
        field_position = (self.__field_x, self.__field_y, self.__field_width, self.__field_height)
        self.__field_renderer.render(*field_position)
        self.__worm_renderer.render(self.__worm, self.__field_x, self.__field_y)

        self.__worm.move()
