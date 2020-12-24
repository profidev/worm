import pygame

from src.gameround import GameRound


class GameProcessor:
    def __init__(self):
        pygame.init()
        size = [800, 600]
        self.__screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Игра червячок для Златки :)")

    def run(self):
        game_round = GameRound(self.__screen)
        game_round.main_loop()
        print('Game over!');

    def __del__(self):
        pygame.quit()
