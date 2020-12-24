from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Worm:
    def __init__(self, initial_length, max_length, position_x, position_y, cell_size):
        self.__direction = Direction.LEFT
        self.__length = initial_length
        self.__max_length = max_length
        self.__x = position_x
        self.__y = position_y
        self.__cell_size = cell_size

    def move(self):
        if self.__direction == Direction.LEFT:
            self.__x -= self.__cell_size
        if self.__direction == Direction.RIGHT:
            self.__x += self.__cell_size
        if self.__direction == Direction.UP:
            self.__y -= self.__cell_size
        if self.__direction == Direction.DOWN:
            self.__y += self.__cell_size

    def get_position(self):
        return self.__x, self.__y

    def get_length(self):
        pass
