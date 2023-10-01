import pygame.font
from pygame.sprite import Group
from Ship import Lives

class Button:
    def __init__(self, AI_game, msg):
        """Initialize button attributes."""
        self.screen = AI_game.screen
        self.screen_rect = self.screen.get_rect()
        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class GameStats:
    """Track statistics for Alien Invasion."""
    def __init__(self, AI_game):
        """Initialize statistics."""
        self.settings = AI_game.settings
        self.reset_stats()
        # Start Alien Invasion in an active state.
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

class Scoreboard:
    """A class to report scoring information."""
    def __init__(self, AI_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = AI_game
        self.screen = AI_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = AI_game.settings
        self.stats = AI_game.stats
        # Font settings for scoring information.
        self.text_color_score = (255, 0, 0)
        self.text_color_level = (64, 224, 208)
        self.text_color_life = (247, 229, 11)
        self.font = pygame.font.SysFont(None, 48)
        # Prepare the initial score image.
        self.prep_score()
        # Prepare the initial level image
        self.prep_level()
        # Prepare the lives
        self.prep_lives()

    def prep_score(self):
        """Turn the score into a rendered image."""
        # Rounding the score
        rounded_score = round(self.stats.score, -1)
        score_str = "Score: "
        score_str += "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color_score, self.settings.bg_color)
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = "Level: "
        level_str += str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color_level, self.settings.bg_color)
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = self.screen_rect.centerx
        self.level_rect.top = self.score_rect.top

    def prep_lives(self):
        """Show how many lives are left."""
        life_str = "Lives: "
        self.life_image = self.font.render(life_str, True, self.text_color_life, self.settings.bg_color)
        # Position the level below the score.
        self.life_rect = self.life_image.get_rect()
        self.life_rect.left = self.screen_rect.left + 20
        #self.life_rect.centerx = self.screen_rect.centerx
        self.life_rect.top = self.score_rect.top
        self.lives = Group()
        for life_number in range(self.stats.ships_left):
            life = Lives(self.ai_game)
            life.rect.x = 130 + life_number * life.rect.width
            life.rect.y = 20
            self.lives.add(life)

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.life_image, self.life_rect)
        self.lives.draw(self.screen)
