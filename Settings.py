import pygame

class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 700
        self.bgimg = pygame.image.load("Images/Space.jpg")
        self.bgimg = pygame.transform.scale(self.bgimg, (self.screen_width, self.screen_height))
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_width = 7
        self.bullet_height = 21
        self.bullet_color = (0, 255, 0)
        self.bullets_allowed = 5
        self.ship_limit = 3

        # Alien settings
        self.fleet_drop_speed = 5

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        #Audio Settings
        self.game_start_sound = pygame.mixer.Sound("Sounds/GameStart.mp3")
        self.alien_hit_sound = pygame.mixer.Sound("Sounds/AlienHit.mp3")
        self.ship_hit_sound = pygame.mixer.Sound("Sounds/ShipHit.mp3")
        self.game_over_sound = pygame.mixer.Sound("Sounds/GameOver.mp3")
        self.next_level_sound = pygame.mixer.Sound("Sounds/NextLevel.mp3")

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        """ Increasing Points """
        self.alien_points = int(self.alien_points * self.score_scale)
