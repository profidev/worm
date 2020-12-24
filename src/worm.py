from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Worm:
    def __init__(self, initial_length, max_length, position_x, position_y):
        self.__body = []
        self.__init_body(initial_length, position_x, position_y)

        self.__direction = Direction.LEFT
        self.__length = initial_length
        self.__max_length = max_length
        self.__x = position_x
        self.__y = position_y

    def move(self):
        if self.__direction == Direction.LEFT:
            self.__x -= 1
        if self.__direction == Direction.RIGHT:
            self.__x += 1
        if self.__direction == Direction.UP:
            self.__y -= 1
        if self.__direction == Direction.DOWN:
            self.__y += 1

        self.__body.pop()
        self.__body.insert(0, [self.__x, self.__y])

    def get_position(self):
        return self.__x, self.__y

    def get_body(self):
        return self.__body

    def __init_body(self, length, x, y):
        for i in range(length):
            self.__body.append((x + i, y))


