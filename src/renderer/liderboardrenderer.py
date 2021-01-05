import pygame

from src.colors import *


class LeaderboardRenderer:
    def __init__(self, screen):
        self.__screen = screen

    def render(self, leaders):
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

            for i, leader in enumerate(leaders):
                name, score = leader
                block = small_font.render(name + ":   " + str(score), True, WHITE)
                rect = block.get_rect()
                rect.center = self.__screen.get_rect().center
                rect.y = 80 + 50 * i
                self.__screen.blit(block, rect)
            pygame.display.flip()

