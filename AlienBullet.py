import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, AI_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = AI_game.screen
        self.settings = AI_game.settings
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('Images/Alien.jpg')
        self.rect = self.image.get_rect()
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width//2
        self.rect.y = self.rect.height//2
        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to the right."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    def __init__(self, AI_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = AI_game.screen
        self.settings = AI_game.settings
        self.color = self.settings.bullet_color
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = AI_game.ship.rect.midtop
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
