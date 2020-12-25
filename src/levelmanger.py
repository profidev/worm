class LevelManager:
    def __init__(self):
        self.__levels_config = [
            (0.17, 3, 30, 28, 20),
            (0.15, 3, 40, 28, 20),
        ]
        self.__level = 1

    def get_current_level_config(self):
        # TODO: check if level more the amount of configs
        return self.__levels_config[self.__level - 1]

    def increase_level(self):
        self.__level += 1
