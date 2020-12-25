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
            self.__screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True

                self.__field.move(event)

            self.__field.action()
            if self.__field.is_round_finish():
                finished = True

            pygame.display.flip()
