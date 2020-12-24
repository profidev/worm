import pygame
from src.colors import *


class GameRound:
    def __init__(self, screen):
        self.__screen = screen

    def main_loop(self):
        finished = False
        clock = pygame.time.Clock()

        while not finished:
            clock.tick(10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True

            self.__screen.fill(WHITE)
