import pygame
from pygame.sprite import Sprite

class Ship():
    """A class to manage the ship."""
    def __init__(self, AI_game):
        """Initialize the ship and set its starting position."""
        self.screen = AI_game.screen
        self.screen_rect = AI_game.screen.get_rect()
        # Load the ship image and get its rect.
        self.image = pygame.image.load('Images/Ship.jpg')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Store a decimal value for the ship's position. As rect is int but speed is float.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3


    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.ship_speed

        # Update rect object from self.x & self.y.
        self.rect.x = self.x
        self.rect.y = self.y
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

class Lives(Sprite):
    """A class to manage the ship."""
    def __init__(self, AI_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = AI_game.screen
        self.screen_rect = AI_game.screen.get_rect()
        # Load the ship image and get its rect.
        self.image = pygame.image.load('Images/Life.png')
        self.rect = self.image.get_rect()
                
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
