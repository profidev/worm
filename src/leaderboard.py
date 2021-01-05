class Leaderboard:
    __SRC_FILENAME = 'src/leaderboard.dat'
    __DELIMITER = '::'

    def __init__(self, score_processor, text_renderer):
        self.__score_processor = score_processor
        self.__text_renderer = text_renderer

    def get_leaders_list(self):
        leaders = []

        f = open(self.__SRC_FILENAME, 'r')
        for line in f:
            name, score = line.split(self.__DELIMITER)
            leaders.append((name, int(score)))
        f.close()

        if len(leaders) == 0 or min(leaders, key=lambda t: t[1])[1] < self.__score_processor.get_score():
            player_name = self.__text_renderer.input_name()
            if player_name != "":
                leaders.append((player_name, self.__score_processor.get_score()))

        sorted_leaders = sorted(leaders[:10], key=lambda t: t[1], reverse=True)

        f = open(self.__SRC_FILENAME, 'w')
        for name, score in sorted_leaders:
            f.write(name + self.__DELIMITER + str(score) + "\n")
        f.close()

        return sorted_leaders
