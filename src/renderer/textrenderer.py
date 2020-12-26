import time

import pygame

from src.colors import *


class TextRenderer:
    def __init__(self, screen):
        self.__screen = screen
        self.__size_x, self.__size_y = pygame.display.get_window_size()

    def display_slide_text(self, text):
        main_font = pygame.font.SysFont('Impact', 60)
        main_text = main_font.render(text, False, ANTIQUE_WHITE)
        pos_y = round((self.__size_y - 60) / 2)
        for pos_x in range(self.__size_x + 1, round((self.__size_x - main_text.get_width()) / 2), -1):
            self.__screen.fill(BLACK)
            self.__screen.blit(main_text, (pos_x, pos_y))
            pygame.display.flip()
        time.sleep(2)
        for pos_x in range(round((self.__size_x - main_text.get_width()) / 2), - main_text.get_width() - 1, -1):
            self.__screen.fill(BLACK)
            self.__screen.blit(main_text, (pos_x, pos_y))
            pygame.display.flip()

    def display_popup_text(self, text):
        for font_size in range(0, 80):
            main_font = pygame.font.SysFont('Impact', font_size)
            main_text = main_font.render(text, False, RED)
            pos_x = round((self.__size_x - main_text.get_width()) / 2)
            pos_y = round((self.__size_y - main_text.get_height()) / 2)
            self.__screen.fill(BLACK)
            self.__screen.blit(main_text, (pos_x, pos_y))
            pygame.display.flip()
            time.sleep(0.005)
        time.sleep(3)
