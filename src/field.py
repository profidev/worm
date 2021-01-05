import pygame

from src.constants import *
from src.foodfactory import FoodFactory
from src.renderer.fieldrenderer import FieldRenderer
from src.renderer.foodrenderer import FoodRenderer
from src.renderer.wormrenderer import WormRenderer
from src.worm import Worm


class Field:

    def __init__(self, screen, level_manager, score_processor):
        size_x, size_y = pygame.display.get_window_size()
        self.__field_width = FIELD_WIDTH * CELL_SIZE
        self.__field_height = FIELD_HEIGHT * CELL_SIZE
        self.__field_x = round((size_x - self.__field_width) / 2)
        self.__field_y = size_y - self.__field_x - self.__field_height

        self.__field_renderer = FieldRenderer(screen)
        self.__level_manager = level_manager
        self.__worm = Worm(*level_manager.get_current_level_config())
        self.__worm_renderer = WormRenderer(screen)
        self.__foods = []
        self.__food_renderer = FoodRenderer(screen)
        self.__score_processor = score_processor

        self.__is_game_over = False

    def action(self):
        field_position = (self.__field_x, self.__field_y, self.__field_width, self.__field_height)
        self.__field_renderer.render(*field_position)
        self.__field_renderer.write_data(
            self.__score_processor.get_score(),
            len(self.__worm.get_body()),
            self.__level_manager.get_current_level()
        )

        self.__worm.move()
        eat_food = self.__worm.eat(self.__foods)
        if eat_food is not None:
            self.__score_processor.add_points(eat_food.get_points())
        self.__worm_renderer.render(self.__worm, self.__field_x, self.__field_y)

        food = FoodFactory.generate()
        if food is not None and len(self.__foods) < MAX_FOODS_ON_FIELD:
            self.__foods.append(food)
        self.__food_renderer.render(self.__foods, self.__field_x, self.__field_y)
        for i, food in enumerate(self.__foods):
            if food.is_expired():
                del self.__foods[i]

        if self.__worm.is_wall_bump() or self.__worm.is_touch_tail():
            self.__worm_renderer.death(self.__worm, self.__field_x, self.__field_y)
            self.__is_game_over = True

    def is_game_over(self):
        return self.__is_game_over

    def is_level_done(self):
        return self.__worm.is_max_length()

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
