import random

from src.constants import *
from src.food import Banana, Apple, Cherry


class FoodFactory:
    @staticmethod
    def generate():
        if random.randint(0, 1000) < 960:
            return None

        chance = random.randint(0, 100)
        pos_x = random.randint(0, FIELD_WIDTH - 1)
        pos_y = random.randint(0, FIELD_HEIGHT - 1)

        if chance < 60:
            return Banana(pos_x, pos_y)
        elif 60 <= chance < 90:
            return Apple(pos_x, pos_y)
        elif chance >= 90:
            return Cherry(pos_x, pos_y)

