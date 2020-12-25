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

        self.__is_wall_bump = False

    def action(self):
        field_position = (self.__field_x, self.__field_y, self.__field_width, self.__field_height)
        self.__field_renderer.render(*field_position)

        self.__worm.move()
        self.__worm_renderer.render(self.__worm, self.__field_x, self.__field_y)

        if self.__worm.is_wall_bump():
            self.__worm_renderer.death(self.__worm, self.__field_x, self.__field_y)
            self.__is_wall_bump = True

    def is_round_finish(self):
        return self.__is_wall_bump

    def move(self, event):
        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_UP:
            self.__worm.move_up()
        elif event.key == pygame.K_DOWN:
            self.__worm.move_down()
        elif event.key == pygame.K_LEFT:
            self.__worm.move_left()
        elif event.key == pygame.K_RIGHT:
            self.__worm.move_right()
