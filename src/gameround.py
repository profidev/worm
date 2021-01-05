from enum import Enum

import pygame
import pygame_menu

from src.colors import *
from src.field import Field
from src.levelmanger import LevelManager
from src.leaderboard import Leaderboard
from src.renderer.liderboardrenderer import LeaderboardRenderer
from src.scoreprocessor import ScoreProcessor
from src.renderer.textrenderer import TextRenderer


class Stage(Enum):
    MENU = 0
    GAME = 1
    LEADERBOARD = 2


class GameRound:
    def __init__(self, screen):
        self.__screen = screen
        self.__level_manger = LevelManager()
        self.__score_processor = ScoreProcessor()
        self.__field = Field(self.__screen, self.__level_manger, self.__score_processor)
        self.__text_renderer = TextRenderer(screen)
        self.__stage = Stage.MENU

    def main_loop(self):
        finished = False
        is_round_started = False
        is_pause = False
        clock = pygame.time.Clock()

        while not finished:
            clock.tick(60)

            if self.__stage == Stage.MENU:
                menu = pygame_menu.Menu(300, 400, 'Menu', theme=pygame_menu.themes.THEME_DARK)

                def start_game():
                    self.__stage = Stage.GAME
                    menu.disable()

                def start_leaderboard():
                    self.__stage = Stage.LEADERBOARD
                    menu.disable()

                menu.add_button('Play', start_game)
                menu.add_button('Leaderboard', start_leaderboard)
                menu.add_label('')
                menu.add_button('Quit', pygame_menu.events.EXIT)

                menu.mainloop(self.__screen, disable_loop=self.__stage is not Stage.MENU)

            elif self.__stage == Stage.GAME:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        finished = True
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            is_pause = not is_pause
                        elif event.key == pygame.K_ESCAPE:
                            finished = True

                    self.__field.move(event)

                if is_pause:
                    continue

                self.__screen.fill(BLACK)

                if not is_round_started:
                    self.__text_renderer.display_slide_text('Level ' + str(self.__level_manger.get_current_level()))
                    is_round_started = True

                self.__field.action()
                if self.__field.is_game_over():
                    self.__text_renderer.display_popup_text('Game over')
                    self.__stage = Stage.LEADERBOARD
                if self.__field.is_level_done():
                    self.__text_renderer.display_slide_text(
                        'Level ' + str(self.__level_manger.get_current_level()) + ' completed'
                    )
                    if self.__level_manger.is_max_level():
                        self.__stage = Stage.LEADERBOARD
                    else:
                        self.__level_manger.increase_level()
                        self.__field = Field(self.__screen, self.__level_manger, self.__score_processor)
                        is_round_started = False
            else:
                leaderboard = Leaderboard(self.__score_processor, self.__text_renderer)
                leaderboard_renderer = LeaderboardRenderer(self.__screen)
                leaderboard_renderer.render(leaderboard.get_leaders_list())
                self.__stage = Stage.MENU

            pygame.display.flip()
