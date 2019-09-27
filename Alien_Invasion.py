import pygame
from pygame.sprite import Group
from Settings import Settings
from Scoreboard import GameStats
from Scoreboard import Scoreboard
from Button import Button
from Ship import Ship
import Functionality as Functionality


def run_game():
    # Initialize pygame
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init()

    # Initialize settings, scoreboard, and stats
    ai_settings = Settings()

    # Initialize game song
    space_invaders_wav = pygame.mixer.Sound('Sounds/spaceinvaders.wav')
    space_invaders_wav.play(-1)

    # Set up the screen to display to user
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create a play button
    play_button = Button(screen, "Play")

    # Initialize the scoreboard and stats
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Create the objects in game
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens
    Functionality.create_fleet(ai_settings, screen, ship, aliens)

    # While Loop - controls updates of the game until user exits screen (or presses q)
    while True:
        Functionality.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            Functionality.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            Functionality.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        Functionality.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


if __name__ == '__main__':
    run_game()
