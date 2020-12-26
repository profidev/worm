class LevelManager:
    def __init__(self):
        self.__levels_config = [
            (0.170, 3, 20, 28, 20),
            (0.165, 3, 23, 28, 20),
            (0.160, 3, 26, 28, 20),
            (0.155, 3, 31, 28, 20),
            (0.150, 3, 35, 28, 20),
            (0.145, 3, 40, 28, 20),
            (0.140, 3, 42, 28, 20),
            (0.135, 4, 44, 28, 20),
            (0.130, 4, 46, 28, 20),
            (0.125, 4, 48, 28, 20),
            (0.120, 4, 50, 28, 20),
            (0.115, 4, 53, 28, 20),
            (0.110, 4, 56, 28, 20),
            (0.100, 4, 60, 28, 20),
            (0.095, 5, 65, 27, 20),
            (0.090, 5, 67, 27, 20),
            (0.085, 5, 68, 27, 20),
            (0.080, 5, 70, 27, 20),
            (0.075, 5, 72, 27, 20),
            (0.070, 5, 74, 27, 20),
            (0.065, 5, 76, 27, 20),
            (0.060, 5, 77, 27, 20),
            (0.055, 5, 78, 27, 20),
            (0.050, 5, 79, 27, 20),
            (0.045, 5, 80, 27, 20),
        ]
        self.__level = 1

    def get_current_level_config(self):
        if self.__level > len(self.__levels_config):
            return None
        return self.__levels_config[self.__level - 1]

    def increase_level(self):
        if self.__level == len(self.__levels_config):
            return
        self.__level += 1

    def get_current_level(self):
        return self.__level

    def is_max_level(self):
        return self.__level >= len(self.__levels_config)
