import pygame

from src.constants import CELL_SIZE


class FoodRenderer:
    def __init__(self, screen):
        self.__screen = screen

    def render(self, foods, field_x, field_y):
        for food in foods:
            x, y = food.get_position()
            pos_x = x * CELL_SIZE + field_x
            pos_y = y * CELL_SIZE + field_y

            image = pygame.image.load("src/renderer/images/" + food.get_image_name())
            image = pygame.transform.scale(image, (10, 10))
            self.__screen.blit(image, (pos_x, pos_y))

