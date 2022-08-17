"""
    game setup and startup
"""

import sys
import pygame
from meadow_valley.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from meadow_valley.level import Level


class Game:
    """Game configuration"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Meadow Valley')
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        """game startup"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            date_time = self.clock.tick() / 1000
            self.level.run(date_time)
            pygame.display.update()
