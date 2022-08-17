"""
    Application startup
"""

from meadow_valley.game import Game


def main():
    """start"""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
