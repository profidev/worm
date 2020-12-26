import pygame

from src.colors import *


class Leaderboard:
    def __init__(self, screen, score_processor):
        self.__screen = screen
        self.__score_processor = score_processor
        self.__name = ""

    def process(self):
        leaders = {}

        f = open('src/leaderboard.dat', 'r')
        for line in f:
            name, score = line.split('::')
            leaders[name] = int(score)
        f.close()

        if min(leaders.values()) < self.__score_processor.get_score():
            self.__input_name()
            if self.__name != "":
                leaders[self.__name] = self.__score_processor.get_score()

        sorted_leaders = {}
        sorted_keys = sorted(leaders, key=leaders.get, reverse=True)
        for i, w in enumerate(sorted_keys):
            if i > 10:
                continue
            sorted_leaders[w] = leaders[w]

        f = open('src/leaderboard.dat', 'w')
        for key in sorted_leaders:
            f.write(key + "::" + str(sorted_leaders[key]) + "\n")
        f.close()

        self.__display_board(sorted_leaders)

    def __display_board(self, leaders):
        font = pygame.font.SysFont('Impact', 50)
        small_font = pygame.font.SysFont('Impact', 35)

        finished = False
        while not finished:
            for evt in pygame.event.get():
                if evt.type == pygame.KEYDOWN:
                    if evt.key == pygame.K_ESCAPE:
                        finished = True
                elif evt.type == pygame.QUIT:
                    return
            self.__screen.fill(BLACK)
            text = font.render('Лучший счет', False, WHITE)
            rect = text.get_rect()
            rect.center = self.__screen.get_rect().center
            rect.y = 10
            self.__screen.blit(text, rect)

            for i, key in enumerate(leaders):
                block = small_font.render(key + ":   " + str(leaders[key]), True, WHITE)
                rect = block.get_rect()
                rect.center = self.__screen.get_rect().center
                rect.y = 80 + 50 * i
                self.__screen.blit(block, rect)
            pygame.display.flip()

    def __input_name(self):
        name = ""
        font = pygame.font.SysFont('Impact', 50)
        is_input_finished = False
        while not is_input_finished:
            for evt in pygame.event.get():
                if evt.type == pygame.KEYDOWN:
                    if evt.unicode.isalpha() or pygame.K_0 <= evt.key <= pygame.K_9:
                        name += evt.unicode
                    elif evt.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    elif evt.key == pygame.K_RETURN:
                        is_input_finished = True
                elif evt.type == pygame.QUIT:
                    return
            self.__screen.fill(BLACK)
            text = font.render('Введи ваше имя', False, WHITE)
            rect = text.get_rect()
            rect.center = self.__screen.get_rect().center
            rect.y -= 60
            self.__screen.blit(text, rect)

            block = font.render(name, True, WHITE)
            rect = block.get_rect()
            rect.center = self.__screen.get_rect().center
            self.__screen.blit(block, rect)
            pygame.display.flip()
        self.__name = name
