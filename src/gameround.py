from enum import Enum

import pygame

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

    def main_loop(self):
        finished = False
        is_round_started = False
        is_pause = False
        stage = Stage.GAME
        clock = pygame.time.Clock()

        while not finished:
            clock.tick(60)

            if stage == Stage.MENU:
                pass
            elif stage == Stage.GAME:
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
                    stage = Stage.LEADERBOARD
                if self.__field.is_level_done():
                    self.__text_renderer.display_slide_text(
                        'Level ' + str(self.__level_manger.get_current_level()) + ' completed'
                    )
                    if self.__level_manger.is_max_level():
                        stage = Stage.LEADERBOARD
                    else:
                        self.__level_manger.increase_level()
                        self.__field = Field(self.__screen, self.__level_manger, self.__score_processor)
                        is_round_started = False
            else:
                leaderboard = Leaderboard(self.__score_processor, self.__text_renderer)
                leaderboard_renderer = LeaderboardRenderer(self.__screen)
                leaderboard_renderer.render(leaderboard.get_leaders_list())
                finished = True

            pygame.display.flip()
