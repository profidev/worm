import pygame

from src.colors import *
from src.field import Field
from src.levelmanger import LevelManager


class GameRound:
    def __init__(self, screen):
        self.__screen = screen
        self.__level_manager = LevelManager()
        self.__field = Field(self.__screen, self.__level_manager)

    def main_loop(self):
        finished = False
        clock = pygame.time.Clock()

        while not finished:
            clock.tick(5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True

            self.__screen.fill(BLACK)

            self.__field.action()

            pygame.display.flip()
