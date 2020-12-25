class ScoreProcessor:
    def __init__(self):
        self.__score = 0

    def add_points(self, points):
        self.__score += points

    def get_score(self):
        return self.__score
