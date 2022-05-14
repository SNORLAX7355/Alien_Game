import pygame

class Ship:
    """ship management"""

    def __init__(self, ai_game):
        """initialize ship and set start position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load ship image and get rect
        self.image = pygame.image.load('Alien Game\images\ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship's position based on movement flag"""
        #update ship x value, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center ship on screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)