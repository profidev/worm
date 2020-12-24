class LevelManager:
    def __init__(self):
        self.__levels_config = [
            (3, 10, 28, 20),
            (3, 15, 28, 20),
        ]
        self.__level = 1

    def get_current_level_config(self):
        # TODO: check if level more the amount of configs
        return self.__levels_config[self.__level - 1]

    def increase_level(self):
        self.__level += 1
