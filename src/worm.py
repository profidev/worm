import time
from enum import Enum

from src.constants import *


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Worm:
    def __init__(self, step_delay, initial_length, max_length, position_x, position_y):
        self.__body = []
        self.__init_body(initial_length, position_x, position_y)

        self.__direction = Direction.LEFT
        self.__length = initial_length
        self.__max_length = max_length
        self.__x = position_x
        self.__y = position_y
        self.__step_delay = step_delay

        self.__is_wall_bump = False
        self.__is_touch_tail = False
        self.__is_eat = False

    def move(self):
        time.sleep(self.__step_delay)

        if self.__direction == Direction.LEFT:
            self.__x -= 1
            if self.__x < 0:
                self.__x = 0
                self.__is_wall_bump = True
        if self.__direction == Direction.RIGHT:
            self.__x += 1
            if self.__x > FIELD_WIDTH - 1:
                self.__x = FIELD_WIDTH - 1
                self.__is_wall_bump = True
        if self.__direction == Direction.UP:
            self.__y -= 1
            if self.__y < 0:
                self.__y = 0
                self.__is_wall_bump = True
        if self.__direction == Direction.DOWN:
            self.__y += 1
            if self.__y > FIELD_HEIGHT - 1:
                self.__y = FIELD_HEIGHT - 1
                self.__is_wall_bump = True

        for body_cell in self.__body:
            body_cell_x, body_cell_y = body_cell
            if self.__x == body_cell_x and self.__y == body_cell_y:
                self.__is_touch_tail = True
                return

        if self.__is_wall_bump:
            return

        if not self.__is_eat:
            self.__body.pop()
        else:
            self.__is_eat = False
        self.__body.insert(0, [self.__x, self.__y])

    def get_position(self):
        return self.__x, self.__y

    def get_direction(self):
        return self.__direction

    def get_body(self):
        return self.__body

    def __init_body(self, length, x, y):
        for i in range(length):
            self.__body.append((x + i, y))

    def move_up(self):
        if self.__direction is not Direction.DOWN:
            self.__direction = Direction.UP

    def move_down(self):
        if self.__direction is not Direction.UP:
            self.__direction = Direction.DOWN

    def move_left(self):
        if self.__direction is not Direction.RIGHT:
            self.__direction = Direction.LEFT

    def move_right(self):
        if self.__direction is not Direction.LEFT:
            self.__direction = Direction.RIGHT

    def is_wall_bump(self):
        return self.__is_wall_bump

    def is_touch_tail(self):
        return self.__is_touch_tail

    def eat(self, foods):
        for i, food in enumerate(foods):
            if (self.__x, self.__y) == food.get_position():
                self.__is_eat = True
                del foods[i]
                return food
        return None
