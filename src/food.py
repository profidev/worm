import time


class Food:
    def __init__(self, lifetime, points, pos_x, pos_y):
        self.__time_to_remove = time.time() + lifetime
        self.__points = points
        self.__x = pos_x
        self.__y = pos_y

    def is_expired(self):
        return time.time() > self.__time_to_remove

    def get_position(self):
        return self.__x, self.__y

    def get_points(self):
        return self.__points

    def get_image_name(self):
        pass


class Banana(Food):
    def __init__(self, pos_x, pos_y):
        super().__init__(20, 10, pos_x, pos_y)

    def get_image_name(self):
        return 'bananas.png'


class Apple(Food):
    def __init__(self, pos_x, pos_y):
        super().__init__(10, 20, pos_x, pos_y)

    def get_image_name(self):
        return 'apple.png'


class Cherry(Food):
    def __init__(self, pos_x, pos_y):
        super().__init__(5, 50, pos_x, pos_y)

    def get_image_name(self):
        return 'cherry.png'
